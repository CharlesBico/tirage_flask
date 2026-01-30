import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import os

# ---------------- CONFIGURATION ----------------
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
DB_NAME = "archives.db"

# ---------------- BASE DE DONNÉES ----------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            chemin TEXT NOT NULL,
            categorie TEXT,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()

# ---------------- APPLICATION ----------------
class ArchivageApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Application d'archivage électronique")
        self.geometry("1100x650")
        self.resizable(False, False)

        self.selected_id = None

        self.create_widgets()
        self.load_data()

    # ---------------- INTERFACE ----------------
    def create_widgets(self):
        frame_form = ctk.CTkFrame(self)
        frame_form.pack(fill="x", padx=10, pady=10)

        # Champs
        ctk.CTkLabel(frame_form, text="Nom du document").grid(row=0, column=0, sticky="w")
        self.ent_nom = ctk.CTkEntry(frame_form, width=300)
        self.ent_nom.grid(row=0, column=1, padx=5)

        ctk.CTkLabel(frame_form, text="Chemin du fichier").grid(row=0, column=2, sticky="w")
        self.ent_chemin = ctk.CTkEntry(frame_form, width=300)
        self.ent_chemin.grid(row=0, column=3, padx=5)
        ctk.CTkButton(frame_form, text="Parcourir", command=self.parcourir).grid(row=0, column=4, padx=5)

        ctk.CTkLabel(frame_form, text="Catégorie").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_categorie = ctk.CTkEntry(frame_form, width=300)
        self.ent_categorie.grid(row=1, column=1)

        ctk.CTkLabel(frame_form, text="Description").grid(row=1, column=2, sticky="w")
        self.ent_description = ctk.CTkEntry(frame_form, width=300)
        self.ent_description.grid(row=1, column=3)

        # Boutons
        frame_btn = ctk.CTkFrame(self)
        frame_btn.pack(fill="x", padx=10)

        ctk.CTkButton(frame_btn, text="Nouveau", command=self.nouveau).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Enregistrer", command=self.enregistrer).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Modifier", command=self.modifier).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Supprimer", command=self.supprimer).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Ouvrir", command=self.ouvrir).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Données", command=self.load_data).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Fermer", fg_color="red", command=self.quit).pack(side="right", padx=5)

        # Tableau
        frame_table = ctk.CTkFrame(self)
        frame_table.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("id", "nom", "chemin", "categorie", "description")
        self.table = ttk.Treeview(frame_table, columns=columns, show="headings")

        for col in columns:
            self.table.heading(col, text=col.capitalize())
            self.table.column(col, width=200 if col != "id" else 50)

        self.table.pack(fill="both", expand=True)
        self.table.bind("<<TreeviewSelect>>", self.select_item)

    # ---------------- FONCTIONS ----------------
    def parcourir(self):
        fichier = filedialog.askopenfilename()
        if fichier:
            self.ent_chemin.delete(0, tk.END)
            self.ent_chemin.insert(0, fichier)
            self.ent_nom.delete(0, tk.END)
            self.ent_nom.insert(0, os.path.basename(fichier))

    def nouveau(self):
        self.selected_id = None
        for ent in [self.ent_nom, self.ent_chemin, self.ent_categorie, self.ent_description]:
            ent.delete(0, tk.END)

    def enregistrer(self):
        nom = self.ent_nom.get()
        chemin = self.ent_chemin.get()
        categorie = self.ent_categorie.get()
        description = self.ent_description.get()

        if not nom or not chemin:
            messagebox.showwarning("Attention", "Nom et chemin obligatoires")
            return

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("INSERT INTO documents (nom, chemin, categorie, description) VALUES (?, ?, ?, ?)",
                    (nom, chemin, categorie, description))
        conn.commit()
        conn.close()

        self.load_data()
        self.nouveau()

    def modifier(self):
        if not self.selected_id:
            messagebox.showwarning("Attention", "Aucun document sélectionné")
            return

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("""
            UPDATE documents
            SET nom=?, chemin=?, categorie=?, description=?
            WHERE id=?
        """, (self.ent_nom.get(), self.ent_chemin.get(), self.ent_categorie.get(), self.ent_description.get(), self.selected_id))
        conn.commit()
        conn.close()
        self.load_data()

    def supprimer(self):
        if not self.selected_id:
            return
        if not messagebox.askyesno("Confirmation", "Supprimer ce document ?"):
            return

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("DELETE FROM documents WHERE id=?", (self.selected_id,))
        conn.commit()
        conn.close()
        self.load_data()
        self.nouveau()

    def ouvrir(self):
        chemin = self.ent_chemin.get()
        if chemin and os.path.exists(chemin):
            os.startfile(chemin)

    def load_data(self):
        for item in self.table.get_children():
            self.table.delete(item)

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        for row in cur.execute("SELECT * FROM documents"):
            self.table.insert("", tk.END, values=row)
        conn.close()

    def select_item(self, event):
        selected = self.table.focus()
        values = self.table.item(selected, "values")
        if values:
            self.selected_id = values[0]
            self.ent_nom.delete(0, tk.END)
            self.ent_nom.insert(0, values[1])
            self.ent_chemin.delete(0, tk.END)
            self.ent_chemin.insert(0, values[2])
            self.ent_categorie.delete(0, tk.END)
            self.ent_categorie.insert(0, values[3])
            self.ent_description.delete(0, tk.END)
            self.ent_description.insert(0, values[4])


if __name__ == "__main__":
    init_db()
    app = ArchivageApp()
    app.mainloop()
