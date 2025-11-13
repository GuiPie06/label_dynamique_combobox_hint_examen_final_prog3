import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

DB_PATH = "people.db"

class Gestionnaire_Stock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de Stock")
        self.geometry("700x500")
        self.selected_id = None
        self.selected_id = None
        self.widgets()
        # self.init_db()
        # self._load_rows()
        # self._update_buttons()


    def widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)




        self.labelFrame_fiche_article =  ttk.LabelFrame(self, text="Fiche article")
        self.labelFrame_fiche_article.grid(row=0, column=0, sticky="nsew")
        self.labelFrame_fiche_article.columnconfigure(0, weight=1)
        self.labelFrame_fiche_article.rowconfigure(0, weight=1)
        self.labelFrame_fiche_article.rowconfigure(1, weight=2)

        self.label_statut=(ttk.Label(self.labelFrame_fiche_article, text="Statut"))
        self.label_statut.grid(row=0, column=0, sticky="w")
        self.label_ISBN=(ttk.Label(self.labelFrame_fiche_article, text="ISbn"))
        self.label_ISBN.grid(row=1, column=0, sticky="w")
        self.label_titre=(ttk.Label(self.labelFrame_fiche_article, text="Titre"))
        self.label_titre.grid(row=2, column=0, sticky="w")
        self.label_auteur=(ttk.Label(self.labelFrame_fiche_article, text="Auteur"))
        self.label_auteur.grid(row=3, column=0, sticky="w")
        self.label_quantite=(ttk.Label(self.labelFrame_fiche_article, text="Quantité à acheter"))
        self.label_quantite.grid(row=4, column=0, sticky="w")

        self.statut_combo = tk.StringVar(value="Achat")
        self.entry_statut = ttk.Combobox(self.labelFrame_fiche_article, values=("Achat", "Vente"), state="readonly", textvariable=self.statut_combo )
        self.entry_statut.grid(row=0, column=1, sticky="e")
        self.ent_ISBN = ttk.Entry(self.labelFrame_fiche_article, )
        self.ent_ISBN.grid(row=1, column=1, sticky="e")
        self.ent_titre = ttk.Entry(self.labelFrame_fiche_article, )
        self.ent_titre.grid(row=2, column=1, sticky="e")
        self.ent_auteur = ttk.Entry(self.labelFrame_fiche_article, )
        self.ent_auteur.grid(row=3, column=1, sticky="e")
        self.ent_quantite = ttk.Entry(self.labelFrame_fiche_article, )
        self.ent_quantite.grid(row=4, column=1, sticky="e")

        if self.entry_statut.get == "Achat":
            self.label_statut.configure(text="Quantité à acheter")

        if self.entry_statut.get == "Vente":
            self.label_statut.configure(text="Quantité à vendre")

        self.labelFrame_outils_gestion = ttk.LabelFrame(self.labelFrame_fiche_article, text="Outils de gestion")
        self.labelFrame_fiche_article.grid(row=5, column=0, columnspan=2, sticky="nswe")



        self.frame_tree = tk.Frame(self)
        self.frame_tree.grid(row=0, column=1)
        self.frame_tree.columnconfigure(0, weight=1)
        self.frame_tree.rowconfigure(0, weight=1)

if __name__ == "__main__":
    Gestionnaire_Stock().mainloop()