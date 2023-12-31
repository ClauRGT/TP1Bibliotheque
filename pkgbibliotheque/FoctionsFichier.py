from pkgbibliotheque.GestionPersonne import *
from pkgbibliotheque.GestionDocument import *
from pkgbibliotheque.GestionBiblio import *
import csv

def lire_Adherents(fichier):
    liste_Adherents = []
    with open(fichier,'r') as fich:
        reader = csv.reader(fich, delimiter=';')
        for ligne in reader:
            nom = ligne[0]
            prenom = ligne[1]
            age = ligne[2]
            num = ligne[3]
            liste_Adherents.append(Adherent(Personne(nom, prenom, age), num))
    return liste_Adherents

def save_Adherents(fichier, liste):
    with open(fichier, mode = 'w', newline = '') as fich:
        writer = csv.writer(fich, delimiter = ';')
        for x in liste:
            ligne = [x.nom, x.prenom, x.age, x.num_adherent]
            writer.writerow(ligne)

def lire_Documents(fichier):
    liste_documents = []
    with open(fichier,'r') as fich:
        reader = csv.reader(fich, delimiter=';')
        for ligne in reader:
            if ligne[0] == 'Journal':
                #type = ligne[0]
                titre = ligne[1]
                date_publication = ligne[2]
                liste_documents.append(Journal(Document(titre), date_publication))
            elif ligne[0] == 'Volume':
                if ligne[1] == 'Livre':
                    #type = ligne[0]
                    #sous_class = ligne[1]
                    titre = ligne[2]
                    auteur = ligne[3]
                    dispo = ligne[4]
                    liste_documents.append(Livre(Volume(Document(titre),auteur),dispo))
                elif ligne[1] == 'BandeDessine':
                    #type = ligne[0]
                    #sous_class = ligne[1]
                    titre = ligne[2]
                    auteur = ligne[3]
                    liste_documents.append(BandeDessine(Volume(Document(titre),auteur)))
                elif ligne[1] == 'Dictionnaire':
                    #type = ligne[0]
                    #sous_class = ligne[1]
                    titre = ligne[2]
                    auteur = ligne[3]
                    liste_documents.append(Dictionnaire(Volume(Document(titre),auteur)))

    return liste_documents

def save_Documents(fichier, liste):
    with open(fichier, mode = 'w', newline = '') as fich:
        writer = csv.writer(fich, delimiter = ';')
        for x in liste:
            if x.type == 'Journal':
                ligne = [x.type, x.titre, x.date_publication]
                writer.writerow(ligne)
            elif x.type == 'Volume':
                if x.sous_class == 'Livre':
                    ligne = [x.type, x.sous_class, x.titre, x.auteur, x.dispo]
                    writer.writerow(ligne)
                elif x.sous_class == 'BandeDessine':
                    ligne = [x.type, x.sous_class, x.titre, x.auteur]
                    writer.writerow(ligne)
                elif x.sous_class == 'Dictionnaire':
                    ligne = [x.type, x.sous_class, x.titre, x.auteur]
                    writer.writerow(ligne)

def lire_Emprunts(fichier):
    liste_Emprunts = []
    with open(fichier,'r') as fich:
        reader = csv.reader(fich, delimiter=';')
        for ligne in reader:
            titre = ligne[0]
            nom = ligne[1]
            prenom = ligne[2]
            date_pret = ligne[3]
            date_retour = ligne[4]
            liste_Emprunts.append(Emprunt(titre, nom, prenom, date_pret, date_retour))
    return liste_Emprunts

def save_Emprunts(fichier, liste):
    with open(fichier, mode = 'w', newline ='') as fich:
        writer = csv.writer(fich, delimiter = ';')
        for x in liste:
            ligne = [x.titre, x.nom, x.prenom, x.date_pret, x.date_retour]
            writer.writerow(ligne)