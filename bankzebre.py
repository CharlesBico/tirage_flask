import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import json
import os
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors

class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion Bancaire - Dépôt / Retrait")
        self.root.geometry("950x600")

        self.balance = 0.0
        self.operations = []
        self.selected_iid = None

        self._load_data()
        self.recalc_balances()
        self._build_ui()
        self.refresh_treeview()
        self._update_balance_label()
        self._set_info_message_initial()

    # ----------------- Chargement / sauvegarde -----------------
    def _load_data(self):
        if os.path.exists('operations.json'):
            try:
                with open('operations.json', 'r', encoding='utf-8') as f:
                    self.operations = json.load(f)
            except:
                self.operations = []
        else:
            self.operations = []

    def _save_data(self):
        try:
            with open('operations.json', 'w', encoding='utf-8') as f:
                json.dump(self.operations, f, ensure_ascii=False, indent=2)
        except:
            pass

    # ----------------- Calcul du solde -----------------
    def recalc_balances(self):
        solde = 0
        self.operations.sort(key=lambda x: x['date'])
        for op in self.operations:
            if op['type'] == 'Dépôt':
                solde += op['amount']
            else:
                solde -= op['amount']
            op['balance'] = solde
        self.operations.sort(key=lambda x: x['date'], reverse=True)
        self.balance = self.operations[0]['balance'] if self.operations else 0
        self._save_data()

    # ----------------- Interface -----------------
    def _build_ui(self):
        frm_top = ttk.Frame(self.root, padding=10)
        frm_top.pack(fill=tk.X)

        ttk.Label(frm_top, text="Montant:").grid(row=0, column=0, sticky=tk.W)
        self.amount_var = tk.StringVar()
        ttk.Entry(frm_top, textvariable=self.amount_var, width=45).grid(row=0, column=1, padx=5,sticky=tk.W)

        ttk.Label(frm_top, text="Type:").grid(row=0, column=2, sticky=tk.W)
        self.type_var = tk.StringVar(value="Dépôt")
        type_combo = ttk.Combobox(frm_top, textvariable=self.type_var, values=["Dépôt", "Retrait"], state="readonly", width=17)
        type_combo.grid(row=0, column=3, padx=5)

        ttk.Label(frm_top, text="Description:").grid(row=1, column=0, sticky=tk.W, pady=(8,0))
        self.desc_var = tk.StringVar()
        ttk.Entry(frm_top, textvariable=self.desc_var, width=45).grid(row=1, column=1, sticky=tk.W, padx=5, pady=(8,0))

        btn_frame = ttk.Frame(frm_top)
        btn_frame.grid(row=2, column=0, columnspan=4, pady=12)

        ttk.Button(btn_frame, text="Enregistrer opération", command=self.add_operation).pack(side=tk.LEFT, padx=6)
        ttk.Button(btn_frame, text="Modifier opération", command=self.modify_operation).pack(side=tk.LEFT, padx=6)
        ttk.Button(btn_frame, text="Supprimer sélection", command=self.delete_selected).pack(side=tk.LEFT, padx=6)
        ttk.Button(btn_frame, text="Exporter Excel", command=self.export_excel).pack(side=tk.LEFT, padx=6)
        ttk.Button(btn_frame, text="Exporter PDF", command=self.export_pdf).pack(side=tk.LEFT, padx=6)
        ttk.Button(btn_frame, text="Exporter CSV", command=self.export_csv).pack(side=tk.LEFT, padx=6)

        # Solde en haut avec montant coloré
        solde_frame = tk.Frame(frm_top)
        solde_frame.grid(row=0, column=4, rowspan=2, padx=20)
        tk.Label(solde_frame, text="Solde: ").pack(side=tk.LEFT)
        self.balance_value_label = tk.Label(solde_frame, text=f"{self.balance:.2f}", font=(None,12,'bold'))
        self.balance_value_label.pack(side=tk.LEFT)

        # Tableau des opérations
        frm_table = ttk.Frame(self.root, padding=(10,0,10,0))
        frm_table.pack(fill=tk.BOTH, expand=True)
        columns = ("date", "type", "amount", "balance", "description")
        self.tree = ttk.Treeview(frm_table, columns=columns, show='headings')
        for col, name in zip(columns, ['Date','Type','Montant','Solde après','Description']):
            self.tree.heading(col, text=name)
        self.tree.column('date', width=150)
        self.tree.column('type', width=80)
        self.tree.column('amount', width=100)
        self.tree.column('balance', width=120)
        self.tree.column('description', width=300)
        vsb = ttk.Scrollbar(frm_table, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(frm_table, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscroll=vsb.set, xscroll=hsb.set)
        self.tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')
        frm_table.rowconfigure(0, weight=1)
        frm_table.columnconfigure(0, weight=1)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Label info message en bas
        self.info_label = tk.Label(self.root, text="", anchor="w", relief=tk.SUNKEN, padx=5)
        self.info_label.pack(fill=tk.X, side=tk.BOTTOM)

    # ----------------- Affichage message -----------------
    def _set_info_message(self, op_type, amount):
        self.info_label.config(text=f"Opération enregistrée: {op_type} {amount:.2f} — Solde: {self.balance:.2f}")

    def _set_info_message_initial(self):
        self.info_label.config(text="Prêt à enregistrer des opérations.")

    # ----------------- Treeview -----------------
    def refresh_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for idx, op in enumerate(self.operations):
            # Zebra background
            zebra_color = '#f9f9f9' if idx%2==0 else '#e6e6e6'
            # Override selon solde
            bg_color = '#d4f4dd' if op['balance'] >= 0 else '#f4d4d4'
            iid = self.tree.insert('', tk.END, values=(
                op['date'], op['type'], f"{op['amount']:.2f}", f"{op['balance']:.2f}", op['description']
            ))
            self.tree.tag_configure(f"bg_{iid}", background=bg_color)
            self.tree.item(iid, tags=(f"bg_{iid}",))

    def _update_balance_label(self):
        self.balance_value_label.config(text=f"{self.balance:.2f}", fg='green' if self.balance>=0 else 'red')

    # ----------------- Sélection -----------------
    def on_tree_select(self, event):
        sel = self.tree.selection()
        if sel:
            iid = sel[0]
            vals = self.tree.item(iid, 'values')
            self.amount_var.set(vals[2])
            self.type_var.set(vals[1])
            self.desc_var.set(vals[4])
            self.selected_iid = iid
        else:
            self.selected_iid = None

    # ----------------- Ajouter -----------------
    def add_operation(self):
        amt_text = self.amount_var.get().strip()
        if not amt_text: messagebox.showwarning("Montant manquant","Veuillez entrer un montant."); return
        try: amount = float(amt_text.replace(',', '.'))
        except: messagebox.showerror("Erreur","Montant invalide."); return
        if amount <= 0: messagebox.showerror("Erreur","Montant doit être > 0."); return
        op_type = self.type_var.get()
        desc = self.desc_var.get().strip()
        op = {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'type': op_type, 'amount': round(amount,2), 'description': desc, 'balance':0}
        self.operations.append(op)
        self.recalc_balances()
        self.refresh_treeview()
        self.amount_var.set('')
        self.desc_var.set('')
        self.selected_iid = None
        self._update_balance_label()
        self._set_info_message(op_type, amount)

    # ----------------- Modifier -----------------
    def modify_operation(self):
        if not self.selected_iid: return
        iid = self.selected_iid
        old_vals = self.tree.item(iid,'values')
        try: new_amount = float(self.amount_var.get().replace(',', '.'))
        except: messagebox.showerror("Erreur", "Montant invalide."); return
        new_type = self.type_var.get()
        new_desc = self.desc_var.get().strip()
        for op in self.operations:
            if op['date'] == old_vals[0]:
                op['amount'] = new_amount
                op['type'] = new_type
                op['description'] = new_desc
                break
        self.recalc_balances()
        self.refresh_treeview()
        self.amount_var.set('')
        self.desc_var.set('')
        self.selected_iid = None
        self._update_balance_label()
        self._set_info_message(new_type, new_amount)

    # ----------------- Supprimer -----------------
    def delete_selected(self):
        sel = self.tree.selection()
        if not sel: return
        if not messagebox.askyesno("Confirmer","Supprimer les opérations sélectionnées ?"): return
        for iid in sel:
            vals = self.tree.item(iid,'values')
            self.operations = [op for op in self.operations if op['date'] != vals[0]]
        self.recalc_balances()
        self.refresh_treeview()
        self._update_balance_label()
        self.info_label.config(text="Opération(s) supprimée(s). Solde recalculé.", fg="black")

    # ----------------- Export -----------------
    def export_excel(self):
        if not self.operations: return
        fpath = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel files','*.xlsx')])
        if not fpath: return
        df = pd.DataFrame(self.operations)[['date','type','amount','balance','description']]
        try: df.to_excel(fpath,index=False)
        except Exception as e: messagebox.showerror("Erreur export", str(e))

    def export_csv(self):
        if not self.operations: return
        fpath = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV files','*.csv')])
        if not fpath: return
        df = pd.DataFrame(self.operations)[['date','type','amount','balance','description']]
        try: df.to_csv(fpath,index=False)
        except Exception as e: messagebox.showerror("Erreur export", str(e))

    def export_pdf(self):
        if not self.operations: return
        fpath = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[('PDF files','*.pdf')])
        if not fpath: return
        data=[['Date','Type','Montant','Solde après','Description']]
        for op in self.operations:
            data.append([op['date'],op['type'],f"{op['amount']:.2f}",f"{op['balance']:.2f}",op['description']])
        try:
            doc = SimpleDocTemplate(fpath,pagesize=landscape(A4))
            table = Table(data,repeatRows=1)
            style = TableStyle([
                ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#d3d3d3')),
                ('TEXTCOLOR',(0,0),(-1,0),colors.black),
                ('ALIGN',(2,1),(3,-1),'RIGHT'),
                ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                ('FONTSIZE',(0,0),(-1,-1),8)
            ])
            table.setStyle(style)
            doc.build([table])
        except Exception as e:
            messagebox.showerror("Erreur export PDF", str(e))


if __name__ == '__main__':
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
