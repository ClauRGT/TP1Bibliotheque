from pkgbibliotheque.GestionDocument_lu import *
from pkgbibliotheque.GestionPersonne_lu import *
from datetime import datetime, timedelta

class Emprunt:
    def __init__(self, titre, nom, prenom, date_pret = datetime.now().date(), date_retour = datetime.now().date() + timedelta(days=15)):
        self.titre = titre
        self.nom = nom
        self.prenom = prenom
        self.date_pret = date_pret
        self.date_retour = date_retour

    def __str__(self):
        return "Livre : " + str(self.titre) + "\tAdherent_nom: " + self.nom + "\tAdherent_prenom: " + self.prenom \
            + "\tDate du pret: " + str(self.date_pret) + "\tDate de retour: " + str(self.date_retour)

    @staticmethod
    def lire_clavier():
        print("------- Saisir Emprunt -------")
        titre = input("Journal.titre: ")
        nom = input("Nom_Adherent: ")
        prenom = input("Prenom_Adherent: ")
        return Emprunt(titre, nom, prenom)
class Biblio:

    def __init__(self):
        self.liste_emprunts = []
        self.liste_doc = []
        self.liste_adherent = []

    def ajouter_document(self, doc_type):
        if doc_type == '1':
            doc = Journal.lire_clavier()
        elif doc_type == '2':
            doc = Livre.lire_clavier()
        elif doc_type == '3':
            doc = BandeDessine.lire_clavier()
        elif doc_type == '4':
            doc = Dictionnaire.lire_clavier()
        self.liste_doc.append(doc)

    def lister_document(self):
        for x in self.liste_doc:
            print(x)

    def supprimer_document(self, adherent):
        self.liste_adherent.remove(adherent)

    def get_document(self, doc_index):
        return self.liste_doc[doc_index]
# ----------------------------------------------

    def ajouter_adherent(self):
        adherent = Adherent.lire_clavier()
        self.liste_adherent.append(adherent)

    def lister_adherent(self):
        for x in self.liste_adherent:
            print(x)

    def supprimer_adherent(self, adherent):
        self.liste_adherent.remove(adherent)

    def get_adherent(self, adherent_index):
        return self.liste_adherent[adherent_index]
# --------------------------------------------------
    def ajouter_emprunt(self, emprunt):
        self.liste_emprunts.append(emprunt)

    def lister_emprunt(self):
        for x in self.liste_emprunts:
            print(x)

    def supprimer_emprunt(self, emprunt):
        self.liste_emprunts.remove(emprunt)

    def get_emprunt(self, emprunt_index):
        return self.liste_adherent[emprunt_index]