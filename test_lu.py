from pkgbibliotheque.GestionPersonne_lu import *
from pkgbibliotheque.FoctionsFichier_lu import *

import csv
def lire_Adherents(fich):
    liste_Adherents = []
    with open(fich,'r') as fich:
        reader = csv.reader(fich, delimiter='\t')
        for ligne in reader:
            nom = ligne[0]
            prenom = ligne[1]
            age = ligne[2]
            num = ligne[3]
            liste_Adherents.append(Adherent(Personne(nom, prenom, age), num))
    return liste_Adherents

liste_a = lire_Adherents('Adherents.csv')
liste_a.append(Adherent(Personne('l1','g1','34'),'11456'))
for x in liste_a:
    print(x)


save_Adherents('abc.csv', liste_a)