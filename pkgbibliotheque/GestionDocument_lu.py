class Document:

    def __init__(self, titre, type_doc,  nbr_pages, isbn):
        self.titre = titre
        self.type_doc = type_doc
        self.nbr_pages = nbr_pages
        self.isbn = isbn

    def __str__(self):
        return "Document | Titre du document: " + self.titre + " Nombre de page : " + str(self.nbr_pages) + \
            " ISBN : " + str(self.isbn)

class Livre(Document):

    def __init__(self, doc, auteur, maison_edit, dispo):
        super().__init__(doc.titre, doc.type_doc, doc.nbr_page, doc.isbn)
        self.auteur = auteur
        self.maison_edit = maison_edit
        self.dispo = dispo

    def __str__(self):
        return "Livre | Titre du livre: " + self.titre + " Nombre de page: " + str(self.nbr_pages) + "ISBN: " + str(self.isbn) + "Auteur: " + self.auteur + " Maison d'édition: " + self.maison_edit

class Journal(Document):
    def __init__(self, doc, date_publication):
        super().__init__(doc.titre, doc.type_doc, doc.nbr_page, doc.isbn)
        self.date_publication = date_publication

    def __str__(self):
        return "Livre | Titre du livre: " + self.titre + " Nombre de page: " + str(self.nbr_pages) + "ISBN: " + str(
            self.isbn) + "Date de publication " + self.date_publication

class BandeDessine(Document):
    def __init__(self, doc, date_publication, dessinateur):
        super().__init__(doc.titre, doc.type_doc, doc.nbr_page, doc.isbn)
        self.date_publication = date_publication
        self.dessinateur = dessinateur

    def __str__(self):
        return "Livre | Titre du livre: " + self.titre + " Nombre de page: " + str(self.nbr_pages) + "ISBN: " + str(self.isbn) + "Date de publication " + self.date_publication

    @staticmethod
    def lire_clavier():
        print("------- Saisir Document -------")
        titre = input("Document.titre: ")
        type_doc = input("Document.type_doc : ")
        nbr_pages = input("Document.nbr_pages: ")
        isbn = input("Document.isbn: ")
        return Document(titre, type_doc, nbr_pages, isbn)
        print(lire_clavier())