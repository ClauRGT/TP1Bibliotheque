# -*- coding:utf-8 -*-
from pkgbibliotheque.GestionBiblio import *
from pkgbibliotheque.GestionPersonne import *
from pkgbibliotheque.GestionDocument import *
from pkgbibliotheque.FoctionsFichier import *

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
        save_Adherents('Adherents.csv', myBiblio.liste_adherent)
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
        save_Adherents('Adherents.csv', myBiblio.liste_adherent)

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
        save_Documents('Documents.csv', myBiblio.liste_doc)

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
        save_Documents('Documents.csv', myBiblio.liste_doc)
        anykey = input()

    elif choix == '6':
        myBiblio.lister_document()
        anykey = input()

    elif choix == '7':
        titre = input("Titre: ").strip()
        trouve_titre = False
        quitter = False
        position = -2
        while trouve_titre == False and quitter == False:
            for x in myBiblio.liste_doc:
                if str(x.titre).strip() == titre and x.dispo == 'Oui':
                    trouve_titre = True
                    position = int(myBiblio.liste_doc.index(x))
            if trouve_titre == False:
                titre = input("Re-Entrez le Titre ou <quit> pour quitter: ").strip()
                if titre == 'quit':
                    quitter = True
        if quitter == False:
            nom = input("Nom_Adherent:").strip()
            prenom = input("Prenom_Adherent:").strip()
            trouve_adherent = False
            while trouve_adherent == False and quitter == False:
                for x in myBiblio.liste_adherent:
                    if str(x.nom).strip() == nom and str(x.prenom).strip() == prenom:
                        trouve_adherent = True
                if trouve_adherent == False:
                    nom = input("Nom_Adherent ou <quit> pour quitter:").strip()
                    prenom = input("Prenom_Adherent ou <quit> pour quitter:").strip()
                    if nom == 'quit' or prenom == 'quit':
                        quitter = True
            if quitter == False:
                empr = Emprunt(titre, nom, prenom)
                myBiblio.liste_doc[position].dispo = 'Non'
                myBiblio.ajouter_emprunt(empr)
                save_Emprunts('Emprunts.csv', myBiblio.liste_emprunts)
                save_Documents('Documents.csv', myBiblio.liste_doc)
                print(empr)
                anykey = input()

    elif choix == '8':
        titre = input("Titre:").strip()
        trouve = False
        position = -2
        for x in myBiblio.liste_emprunts:
            if x.titre == titre:
                myBiblio.supprimer_emprunt(x)
                for y in myBiblio.liste_doc:
                    if y.titre == titre:
                        position = int(myBiblio.liste_doc.index(y))
                        myBiblio.liste_doc[position].dispo = 'Oui'
                trouve = True
                print(x)
                print("Déjà retourné!")
        if trouve == False:
            print("Ne trouve pas le Document!")
        save_Emprunts('Emprunts.csv', myBiblio.liste_emprunts)
        save_Documents('Documents.csv', myBiblio.liste_doc)
        anykey = input()

    elif choix == '9':
        myBiblio.lister_emprunt()
        anykey = input()

