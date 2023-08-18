class Document:
    def __init__(self, titre):
        self.titre = titre

    def __str__(self):
        return "Document | Titre du document: " + self.titre

class Journal(Document):
    def __init__(self, doc, date_publication):
        super().__init__(doc.titre)
        self.date_publication = date_publication
        self.type = 'Journal'
    def __str__(self):
        return "Journal | Titre du journal: " + self.titre + "Date de publication " + self.date_publication

    @staticmethod
    def lire_clavier():
        print("------- Saisir Journal -------")
        titre = input("Journal.titre: ")
        date_publication = input("Journal.date: ")
        return Journal(Document(titre), date_publication)


class Volume(Document):
    def __init__(self, doc, auteur):
        super().__init__(doc.titre)
        self.auteur = auteur

class Livre(Volume):

    def __init__(self, vol, dispo):
        super().__init__(Document(vol.titre), vol.auteur)
        self.dispo = dispo
        self.type = 'Volume'
        self.sous_class = 'Livre'

    def __str__(self):
        return "Livre | Titre du livre: " + self.titre + " Auteur: " + self.auteur + " Disponible: " + self.dispo

    def emprunt(self, dispo):
        self.dispo = dispo

    @staticmethod
    def lire_clavier():
        print("------- Saisir Livre -------")
        titre = input("Livre.titre: ")
        auteur = input("Livre.auteur: ")
        dispo = input("Livre.dispo: ")
        return Livre(Volume(Document(titre), auteur), dispo)


class BandeDessine(Volume):
    def __init__(self, vol, dessinateur):
        super().__init__(Document(vol.titre), vol.auteur)
        self.dessinateur = dessinateur
        self.type = 'Volume'
        self.sous_class = 'Bandedessine'

    def __str__(self):
        return "Bandedessine | Titre du livre: " + self.titre

    @staticmethod
    def lire_clavier():
        print("------- Saisir BandeDessine -------")
        titre = input("BandeDessine.titre: ")
        auteur = input("Livre.auteur: ")
        dessinateur = input("BandeDessine.auteur: ")
        return BandeDessine(Volume(Document(titre), auteur), date_publication, dessinateur)

class Dictionnaire(Volume):
    def __init__(self, vol):
        super().__init__(Document(vol.titre), vol.auteur)
        self.type = 'Volume'
        self.sous_class = 'Dictionnaire'
    def __str__(self):
        return "Dictionnaire | Titre du livre: " + self.titre + " Auteur " + self.auteur