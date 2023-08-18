from pkgbibliotheque.GestionPersonne_lu import *
import csv

def lire_Adherents(fichier):
    liste_Adherents = []
    with open(fichier,'r') as fich:
        reader = csv.reader(fich, delimiter='\t')
        for ligne in reader:
            nom = ligne[0]
            prenom = ligne[1]
            age = ligne[2]
            num = ligne[3]
            liste_Adherents.append(Adherent(Personne(nom, prenom, age), num))
    return liste_Adherents

def save_Adherents(fichier, liste):
    with open(fichier, mode = 'w') as fich:
        writer = csv.writer(fich, delimiter = ';')
        for x in liste:
            ligne = [x.nom, x.prenom, x.age, x.num_adherent]
            writer.writerow(ligne)
