from pkgbibliotheque.GestionDocument_lu import *
from pkgbibliotheque.GestionPersonne_lu import *

class Emprunt:
    def __init__(self, doc, adherent, employe, date_pret, date_retour):
        self.doc = doc
        self.adherent = adherent
        self.employe = employe
        self.date_pret = date_pret
        self.date_retour = date_retour

    def __str__(self):
        return "Livre : " + str(self.doc) + "Adherent: " + self.adherent + "Employé: " + self.employe \
            + "Date du pret: " + self.date_pret + "Date du retour: " + self.date_retour

class Biblio:

    def __init__(self):
        self.liste_emprunts = []
        self.liste_doc = []
        self.liste_adherent = []

    def ajouter_document(self):
        doc = BandeDessine.lire_clavier()
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