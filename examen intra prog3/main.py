import tkinter as tk
from tkinter import ttk as ttk, messagebox, filedialog
import json


class Livre:
    def __init__(self, titre, auteur, categorie, statut):
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.statut = statut


    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Titre du livre doit être une chaîne non vide.")
        self.__titre = value.strip()


    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("L'auteur du livre doit être une chaîne non vide.") #certain noms sont composés de chiffre...
        self.__auteur = value.strip()


    @property
    def categorie(self):
        return self.__categorie

    @categorie.setter
    def categorie(self, value):
        if value == "Roman" or value =="Essai" or value =="Science" or value =="Biographie" or value =="Technologie":
            self.__categorie = value
        else:
            raise ValueError("La categorie du roman doit être parmis Roman Essai Science Biographie Technologie")



    @property
    def statut(self):
        return self.__statut

    @statut.setter
    def statut(self, value):
        if value =="Disponible" or value =="Emprunté":
            self.__statut = value
        else:
            raise ValueError("La categorie du roman doit être parmis Disponible Emprunté")







class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de Bibliothèque")

        self.geometry("925x350")

        self.init_widgets()


    def init_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.columnconfigure(1, weight=2)


        self.labelframe_fiche_du_livre= tk.LabelFrame(self, text="Fiche du livre", relief="ridge", borderwidth=3)
        self.labelframe_fiche_du_livre.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.labelframe_fiche_du_livre.columnconfigure(0, weight=1)
        self.labelframe_fiche_du_livre.columnconfigure(1, weight=2)

        self.lbl_titre = ttk.Label(self.labelframe_fiche_du_livre, text="Titre:")
        self.lbl_titre.grid(row=0, column=0,sticky="w", padx = (5,0), pady = 10)

        self.lbl_auteur = ttk.Label(self.labelframe_fiche_du_livre, text="Auteur:")
        self.lbl_auteur.grid(row=1, column=0,sticky="w", padx = (5,0), pady = 10)

        self.lbl_categorie = ttk.Label(self.labelframe_fiche_du_livre, text="Categorie:")
        self.lbl_categorie.grid(row=2, column=0,sticky="w", padx = (5,0), pady = 10)

        self.lbl_statut = ttk.Label(self.labelframe_fiche_du_livre, text="Statut:")
        self.lbl_statut.grid(row=3, column=0,sticky="w", padx = (5,0), pady = 10)

        self.entry_titre = ttk.Entry(self.labelframe_fiche_du_livre)
        self.entry_titre.grid(row=0, column=1, sticky="we", padx = (0,5), pady = 10)

        self.entry_auteur = ttk.Entry(self.labelframe_fiche_du_livre)
        self.entry_auteur.grid(row=1, column=1, sticky="we", padx = (0,5), pady = 10)

        self.categorie_combo = tk.StringVar(value=None)
        self.lb_categorie = ttk.Combobox(self.labelframe_fiche_du_livre, values= ["Roman", "Essai", "Science", "Biographie", "Technologie"],textvariable=self.categorie_combo, state="readonly")
        self.lb_categorie.grid(row=2, column=1, sticky="we", padx = (0,5), pady = 10)

        self.statut_combo = tk.StringVar(value="Disponible")
        self.lb_statut = ttk.Combobox(self.labelframe_fiche_du_livre, values=["Disponible", "Emprunté"], state="readonly",textvariable=self.statut_combo)
        self.lb_statut.grid(row=3, column=1, sticky="we", padx = (0,5), pady = 10)



        self.labelframe_outils_de_gestion = tk.LabelFrame(self.labelframe_fiche_du_livre, text="Outils de gestion", relief="groove", borderwidth=2)
        self.labelframe_outils_de_gestion.grid(row=4, column=0, columnspan=2, sticky="ews", padx=10, pady=20)
        self.labelframe_outils_de_gestion.columnconfigure(0, weight=1)
        self.labelframe_outils_de_gestion.rowconfigure(0, weight=1)

        self.btn_nouveau = ttk.Button(self.labelframe_outils_de_gestion, text="Nouveau", command=self.nouveau)
        self.btn_nouveau.grid(row=0, column=0, sticky="ew", pady = 10, padx = 5)

        self.btn_ajouter = ttk.Button(self.labelframe_outils_de_gestion, text="Ajouter", command=self.ajouter)
        self.btn_ajouter.grid(row=0, column=1, sticky="ew", pady = 10)

        self.btn_supprimer = ttk.Button(self.labelframe_outils_de_gestion, text="Supprimer", command=self.supprimer )
        self.btn_supprimer.grid(row=0, column=2, sticky="ew", pady = 10,padx = 5)

        self.btn_importer_json = ttk.Button(self.labelframe_outils_de_gestion, text="Importer JSON", command=self.importer_json)
        self.btn_importer_json.grid(row=1, column=0, sticky="ew", pady = (0,10),padx = 5)

        self.btn_exporter_json = ttk.Button(self.labelframe_outils_de_gestion, text="Exporter JSON", command=self.exporter_json)
        self.btn_exporter_json.grid(row=1, column=1, sticky="ew", pady = (0,10))

        self.btn_quitter = ttk.Button(self.labelframe_outils_de_gestion, text="Quitter", command=self.quitter)
        self.btn_quitter.grid(row=1, column=2, sticky="ew", pady = (0,10),padx = 5)



        self.frame_tree = tk.Frame(self, relief="ridge", borderwidth=3)
        self.frame_tree.grid(row=0, column=1, sticky="nsew", pady = 10, padx = 5)
        self.frame_tree.columnconfigure(0, weight=1)
        self.frame_tree.rowconfigure(0, weight=1)

        self.columns = ("titre", "auteur", "categorie", "disponibilite")
        self.tree = ttk.Treeview(self.frame_tree, columns=self.columns, show="headings")
        self.tree.heading("titre", text="Titre")
        self.tree.heading("auteur", text="Auteur")
        self.tree.heading("categorie", text="Catégorie")
        self.tree.heading("disponibilite", text="Disponibilité")
        self.tree.column("titre", width=170)
        self.tree.column("auteur", width=170)
        self.tree.column("categorie", width=125)
        self.tree.column("disponibilite", width=125)
        self.tree.grid(row=0, column=0, sticky="nsew")


    def nouveau(self):
        self.entry_titre.delete(0, tk.END)
        self.entry_auteur.delete(0, tk.END)
        self.categorie_combo = tk.StringVar(value=None)
        self.lb_categorie.config(textvariable=self.categorie_combo)
        self.statut_combo = tk.StringVar(value="Disponible")
        self.lb_statut.config(textvariable=self.statut_combo)
        messagebox.showinfo("Mode Nouveau", "Vous pouvez maintenant ajouter un nouveau livre.")




    def ajouter(self):
        titre = self.entry_titre.get()
        auteur = self.entry_auteur.get()
        categorie = self.categorie_combo.get()
        disponibilite = self.statut_combo.get()

        try:
            livre = Livre(titre, auteur, categorie, disponibilite)
            self.tree.insert("", "end", values=(livre.titre, livre.auteur, livre.categorie, livre.statut))
            self.entry_titre.delete(0, "end")
            self.entry_auteur.delete(0, "end")
            self.lb_categorie.delete(0, "end")
            self.lb_statut.delete(0, "end")
            messagebox.showinfo("Succès", f"Le livre '{titre}' a été ajouté")
        except ValueError as e:
            messagebox.showerror("Erreur de saisie", str(e))


    def supprimer(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Sélection requise", "Veuillez sélectionner un livre à supprimer.")
            return
        for livre in selected:
            self.tree.delete(livre)


    def importer_json(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if not filepath:
            return

        with open(filepath, mode='r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            messagebox.showerror("Erreur JSON", "Le fichier JSON doit contenir une liste d'objets.")
            return

        for item in data:
            produit = Livre(item["titre"], item["auteur"], item["categorie"], item["disponibilite"])
            self.tree.insert("", "end", values=(produit.titre, produit.auteur, produit.categorie, produit.statut))

        messagebox.showinfo("Import JSON terminé", " élément(s) importé(s)")

    def exporter_json(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not filepath:
            return
        data = []
        for row in self.tree.get_children():
            data.append(dict(zip(self.columns, self.tree.item(row)["values"])))
        with open(filepath, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Succès", "Produits sauvegardés en JSON.")


    def quitter(self):
        exit()


if __name__ == "__main__":
    app = App()
    app.mainloop()