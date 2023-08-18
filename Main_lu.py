# -*- coding:utf-8 -*-
from pkgbibliotheque.GestionBiblio_lu import *
from pkgbibliotheque.GestionPersonne_lu import *
from pkgbibliotheque.GestionDocument_lu import *
from pkgbibliotheque.FoctionsFichier_lu import *

def afficher_menu(lenth):
    print('*'*lenth)
    print('*', end = '')
    print(f"{'Bienvenue à votre bibliothèque':^{lenth-2}}", end = '')
    print('*')
    print('*', end = '')
    print(f"{'Faites un choix':^{lenth-2}}", end = '')
    print('*')
    print('*' * lenth)
    liste_menu = ['1    Ajouter adhérent', '2    Supprimer adhérent', '3    Afficher tous les adhérents',
                  '4    Ajouter Document', '5    Supprimer Document', '6    Afficher tous les Documents',
                  '7    Ajouter Emprunts', "8    Retour d'un Emprunt", '9    Afficher tous les Emprunts',
                  'Q    Quitter']
    for x in liste_menu:
        print(f"{'*':<5}", end='')
        print(f"{x:<{lenth - 6}}", end='')
        print('*')
    print('*' * lenth)


lenth = 50
choix = ''
myBiblio = Biblio()
myBiblio.liste_adherent = lire_Adherents('Adherents.csv')
myBiblio.liste_doc = lire_Documents('Documents.csv')
myBiblio.liste_emprunts = lire_Emprunts('Emprunts.csv')

while choix != 'Q':
    afficher_menu(lenth)
    choix = input('Choisissez une action:').strip()

    if choix == '1':
        myBiblio.ajouter_adherent()
    elif choix == '2':
        nom = input("Nom:").strip()
        prenom = input("Prenom:").strip()
        trouve = False
        for x in myBiblio.liste_adherent:
            if x.nom == nom and x.prenom == prenom:
                myBiblio.supprimer_adherent(x)
                trouve = True
                print(x)
                print("Déjà supprimé!")
        if trouve == False:
            print("Ne trouve pas l'adherent!")
        anykey = input()


    elif choix == '3':
        myBiblio.lister_adherent()
        anykey = input()

    elif choix == '4':
        doc_type = input(
            "Type du Document: \n\t 1: Journal\t 2: Livre\t 3:BandeDessine\t 4: Dictionnaire\n Faire votre choix: [1,2,3,4]:").strip()
        while doc_type not in ('1', '2', '3', '4'):
            doc_type = input(
                "Type du Document: \n\t 1: Journal\t 2: Livre\t 3:BandeDessine\t 4: Dictionnaire\n Faire votre choix: [1,2,3,4]:").strip()
        myBiblio.ajouter_document(doc_type)

    elif choix == '5':
        titre = input("Titre:").strip()
        trouve = False
        for x in myBiblio.liste_doc:
            if x.titre == titre:
                myBiblio.supprimer_document(x)
                trouve = True
                print(x)
                print("Déjà supprimé!")
                anykey = input()
        if trouve == False:
            print("Ne trouve pas le Document!")
        anykey = input()

    elif choix == '6':
        myBiblio.lister_document()
        anykey = input()

    elif choix == '7':
        titre = input("Titre: ").strip()
        trouve_titre = False
        position = -2
        while trouve_titre == False:
            for x in myBiblio.liste_doc:
                if x.titre == titre and x.dispo == 'True':
                    trouve_titre = True
                    position = int(myBiblio.liste_doc.index(x))
                else:
                    titre = input("Re-Entrez le Titre: ").strip()
        nom = input("Nom_Adherent:").strip()
        prenom = input("Prenom_Adherent:").strip()
        trouve_adherent = False
        while trouve_adherent == False:
            for x in myBiblio.liste_adherent:
                if x.nom == nom and x.prenom == prenom:
                    trouve_adherent = True
                else:
                    nom = input("Nom_Adherent:").strip()
                    prenom = input("Prenom_Adherent:").strip()
        empr = Emprunt(titre, nom, prenom)
        myBiblio.liste_doc[position].dispo = 'False'
        myBiblio.ajouter_emprunt(empr)

    elif choix == '8':
        titre = input("Titre:").strip()
        trouve = False
        for x in myBiblio.liste_emprunts:
            if x.titre == titre:
                myBiblio.supprimer_emprunt(x)
                trouve = True
                print(x)
                print("Déjà supprimé!")
        if trouve == False:
            print("Ne trouve pas le Document!")
        anykey = input()

    elif choix == '9':
        myBiblio.lister_emprunt()
        anykey = input()
    else:
        choix = input('Choix erroné!  Re-entrez:')
