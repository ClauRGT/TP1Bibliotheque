# -*- coding:utf-8 -*-
from pkgbibliotheque.GestionBiblio import *
from pkgbibliotheque.GestionDocument import *
def afficher_menu(lenth):
    print('*'*lenth)
    print('*', end = '')
    print(f"{'Bienvenue à votre bibliothèque':^{lenth-2}}", end = '')
    print('*')
    print('*', end = '')
    print(f"{'Faites un choix':^{lenth-2}}", end = '')
    print('*')
    print('*' * lenth)
    liste_menu = ('1    Ajouter adhérent', '2    Supprimer adhérent', '3    Afficher tous les adhérents',
                  '4    Ajouter Document', '5    Supprimer Document', '6    Afficher tous les Documents',
                  '7    Ajouter Emprunts', "8    Retour d'un Emprunt", '9    Afficher tous les Emprunts',
                  'Q    Quitter')
    for x in liste_menu:
        print(f"{'*':<5}", end='')
        print(f"{x:<{lenth - 6}}", end='')
        print('*')
    print('*' * lenth)

lenth = 50
choix = ''
myBiblio = Biblio()
while choix != 'Q':
    afficher_menu(lenth)
    choix = input('Choisissez une action:').strip()
    if choix == '1':
        myBiblio.ajouter_adherent()
    elif choix == '2':
        myBiblio.supprimer_adherent()
    elif choix == '3':
        myBiblio.lister_adherent()
    elif choix == '4':
        myDocument = BandeDessine.lire_clavier()
        myBiblio.ajouter_document(myDocument)
    elif choix == '5':
        myBiblio.supprimer_document()
    elif choix == '6':
        myBiblio.lister_document()
        anykey = input()
    elif choix == '7':
        myBiblio.ajouter_emprunt()
    elif choix == '8':
        myBiblio.supprimer_emprunt()
    elif choix == '9':
        myBiblio.lister_emprunt()
    else:
        choix = input('Choix erroné!  Re-entrez:')
