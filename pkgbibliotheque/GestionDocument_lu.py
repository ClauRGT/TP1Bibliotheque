class Document:

    def __init__(self, titre, type_doc,  nbr_pages, isbn):
        self.titre = titre
        self.type_doc = type_doc
        self.nbr_pages = nbr_pages
        self.isbn = isbn

    def __str__(self):
        return "Document | Titre du document: " + self.titre + " Nombre de page : " + str(self.nbr_pages) + \
            " ISBN : " + str(self.isbn)

    @staticmethod
    def lire_clavier():
        print("------- Saisir Document -------")
        titre = input("Document.titre: ")
        type_doc = input("Document.type_doc : ")
        nbr_pages = input("Document.nbr_pages: ")
        isbn = input("Document.isbn: ")
        return Document(titre, type_doc, nbr_pages, isbn)

class Livre(Document):

    def __init__(self, doc, auteur, maison_edit, dispo):
        super().__init__(doc.titre, doc.type_doc, doc.nbr_pages, doc.isbn)
        self.auteur = auteur
        self.maison_edit = maison_edit
        self.dispo = dispo

    def __str__(self):
        return "Livre | Titre du livre: " + self.titre + " Nombre de page: " + str(self.nbr_pages) + "ISBN: " + str(self.isbn) + "Auteur: " + self.auteur + " Maison d'édition: " + self.maison_edit

    def modifier_disponible(self, dispo):
        self.dispo = dispo
    @staticmethod
    def lire_clavier():
        print("------- Saisir Livre -------")
        titre = input("Livre.titre: ")
        type_doc = input("Livre.type_doc : ")
        nbr_pages = input("Livre.nbr_pages: ")
        isbn = input("Livre.isbn: ")
        auteur = input("Livre.auteur: ")
        maison_edit = input("Livre.maison_edit: ")
        dispo = input("Livre.dispo: ")
        return Livre(Document(titre, type_doc, nbr_pages, isbn), auteur, maison_edit, dispo)

class Journal(Document):
    def __init__(self, doc, date_publication):
        super().__init__(doc.titre, doc.type_doc, doc.nbr_pages, doc.isbn)
        self.date_publication = date_publication

    def __str__(self):
        return "Livre | Titre du livre: " + self.titre + " Nombre de page: " + str(self.nbr_pages) + "ISBN: " + str(
            self.isbn) + "Date de publication " + self.date_publication

    @staticmethod
    def lire_clavier():
        print("------- Saisir Journal -------")
        titre = input("Journal.titre: ")
        type_doc = input("Journal.type_doc : ")
        nbr_pages = input("Journal.nbr_pages: ")
        isbn = input("Journal.isbn: ")
        date_publication = input("Journal.date: ")
        return Journal(Document(titre, type_doc, nbr_pages, isbn), date_publication)

class BandeDessine(Document):
    def __init__(self, doc, date_publication, dessinateur):
        super().__init__(doc.titre, doc.type_doc, doc.nbr_pages, doc.isbn)
        self.date_publication = date_publication
        self.dessinateur = dessinateur

    def __str__(self):
        return "Livre | Titre du livre: " + self.titre + " Nombre de page: " + str(self.nbr_pages) + "ISBN: " + str(self.isbn) + "Date de publication " + self.date_publication

    @staticmethod
    def lire_clavier():
        print("------- Saisir BandeDessine -------")
        titre = input("BandeDessine.titre: ")
        type_doc = input("BandeDessine.type_doc : ")
        nbr_pages = input("BandeDessine.nbr_pages: ")
        isbn = input("BandeDessine.isbn: ")
        date_publication = input("BandeDessine.date: ")
        dessinateur = input("BandeDessine.auteur: ")
        return BandeDessine(Document(titre, type_doc, nbr_pages, isbn), date_publication, dessinateur)
