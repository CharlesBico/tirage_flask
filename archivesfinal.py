import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import os
import shutil
from datetime import datetime
from pathlib import Path
import sys

# ================= CONFIGURATION =================
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# ================= CHEMIN PORTABLE SANS ADMIN =================
# Tous les fichiers sont stockés dans Documents pour éviter WinError 5
BASE_DIR = Path.home() / "Documents" / "Archivage Electronique"
BASE_DIR.mkdir(parents=True, exist_ok=True)

ARCHIVE_ROOT = BASE_DIR / "archives"
ARCHIVE_ROOT.mkdir(parents=True, exist_ok=True)

DB_NAME = BASE_DIR / "archives.db"

# ================= BASE DE DONNÉES =================
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

# ================= APPLICATION =================
class ArchivageApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Application d'archivage électronique")
        self.geometry("1200x720")
        self.resizable(True, True)

        self.selected_id = None

        self.create_widgets()
        self.load_data()

    # ================= INTERFACE =================
    def create_widgets(self):
        frame_form = ctk.CTkFrame(self)
        frame_form.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(frame_form, text="Nom du document").grid(row=0, column=0, sticky="w")
        self.ent_nom = ctk.CTkEntry(frame_form, width=300)
        self.ent_nom.grid(row=0, column=1, padx=5)

        ctk.CTkLabel(frame_form, text="Chemin du fichier (original)").grid(row=0, column=2, sticky="w")
        self.ent_chemin = ctk.CTkEntry(frame_form, width=300)
        self.ent_chemin.grid(row=0, column=3, padx=5)
        ctk.CTkButton(frame_form, text="Parcourir", command=self.parcourir).grid(row=0, column=4, padx=5)

        ctk.CTkLabel(frame_form, text="Catégorie").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_categorie = ctk.CTkEntry(frame_form, width=300)
        self.ent_categorie.grid(row=1, column=1)

        ctk.CTkLabel(frame_form, text="Description").grid(row=1, column=2, sticky="w")
        self.ent_description = ctk.CTkEntry(frame_form, width=300)
        self.ent_description.grid(row=1, column=3)

        frame_btn = ctk.CTkFrame(self)
        frame_btn.pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(frame_btn, text="Nouveau", command=self.nouveau).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Enregistrer", command=self.enregistrer).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Modifier", command=self.modifier).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Supprimer", command=self.supprimer).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Ouvrir", command=self.ouvrir).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Données", command=self.load_data).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Ouvrir archives", command=self.ouvrir_archives).pack(side="left", padx=5)
        ctk.CTkButton(frame_btn, text="Fermer", fg_color="red", command=self.quit).pack(side="right", padx=5)

        frame_filter = ctk.CTkFrame(self)
        frame_filter.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(frame_filter, text="Recherche (Nom)").pack(side="left", padx=5)
        self.filter_nom = ctk.CTkEntry(frame_filter, width=220)
        self.filter_nom.pack(side="left", padx=5)

        ctk.CTkLabel(frame_filter, text="Recherche (Catégorie)").pack(side="left", padx=5)
        self.filter_categorie = ctk.CTkEntry(frame_filter, width=220)
        self.filter_categorie.pack(side="left", padx=5)

        self.filter_nom.bind("<KeyRelease>", lambda e: self.filtrer())
        self.filter_categorie.bind("<KeyRelease>", lambda e: self.filtrer())

        ctk.CTkButton(frame_filter, text="Réinitialiser", command=self.reset_filtre).pack(side="left", padx=10)

        frame_table = ctk.CTkFrame(self)
        frame_table.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("id", "nom", "chemin", "categorie", "description")
        self.table = ttk.Treeview(frame_table, columns=columns, show="headings")

        for col in columns:
            self.table.heading(col, text=col.capitalize())
            self.table.column(col, width=200 if col != "id" else 50)

        self.table.pack(fill="both", expand=True)
        self.table.bind("<<TreeviewSelect>>", self.select_item)

    # ================= LOGIQUE =================
    def parcourir(self):
        fichier = filedialog.askopenfilename()
        if fichier:
            self.ent_chemin.delete(0, tk.END)
            self.ent_chemin.insert(0, fichier)
            self.ent_nom.delete(0, tk.END)
            self.ent_nom.insert(0, os.path.basename(fichier))

    def copier_fichier(self, chemin_source, categorie):
        annee = datetime.now().year
        categorie = categorie if categorie else "NonClasse"

        dossier_dest = ARCHIVE_ROOT / str(annee) / categorie
        dossier_dest.mkdir(parents=True, exist_ok=True)

        nom_fichier = os.path.basename(chemin_source)
        chemin_dest = dossier_dest / nom_fichier

        base, ext = os.path.splitext(chemin_dest)
        compteur = 1
        while chemin_dest.exists():
            chemin_dest = Path(f"{base}_{compteur}{ext}")
            compteur += 1

        shutil.copy2(chemin_source, chemin_dest)
        return str(chemin_dest)

    def ouvrir_archives(self):
        if ARCHIVE_ROOT.exists():
            os.startfile(ARCHIVE_ROOT)
        else:
            messagebox.showinfo("Info", "Le dossier archives n'existe pas encore.")

    def nouveau(self):
        self.selected_id = None
        for ent in (self.ent_nom, self.ent_chemin, self.ent_categorie, self.ent_description):
            ent.delete(0, tk.END)

    def enregistrer(self):
        if not self.ent_nom.get() or not self.ent_chemin.get():
            messagebox.showwarning("Attention", "Nom et fichier obligatoires")
            return

        chemin_archive = self.copier_fichier(
            self.ent_chemin.get(),
            self.ent_categorie.get()
        )

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO documents (nom, chemin, categorie, description) VALUES (?, ?, ?, ?)",
            (self.ent_nom.get(), chemin_archive, self.ent_categorie.get(), self.ent_description.get())
        )
        conn.commit()
        conn.close()

        self.load_data()
        self.nouveau()

    def modifier(self):
        if not self.selected_id:
            return

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute(
            "UPDATE documents SET nom=?, categorie=?, description=? WHERE id=?",
            (self.ent_nom.get(), self.ent_categorie.get(), self.ent_description.get(), self.selected_id)
        )
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
        cur.execute("SELECT chemin FROM documents WHERE id=?", (self.selected_id,))
        chemin = cur.fetchone()[0]

        if os.path.exists(chemin):
            os.remove(chemin)

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

    def filtrer(self):
        nom = self.filter_nom.get()
        categorie = self.filter_categorie.get()

        for item in self.table.get_children():
            self.table.delete(item)

        query = "SELECT * FROM documents WHERE 1=1"
        params = []

        if nom:
            query += " AND nom LIKE ?"
            params.append(f"%{nom}%")
        if categorie:
            query += " AND categorie LIKE ?"
            params.append(f"%{categorie}%")

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        for row in cur.execute(query, params):
            self.table.insert("", tk.END, values=row)
        conn.close()

    def reset_filtre(self):
        self.filter_nom.delete(0, tk.END)
        self.filter_categorie.delete(0, tk.END)
        self.load_data()

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
