# -*- coding:utf-8 -*-

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

while choix != 'Q':
    afficher_menu(lenth)
    choix = input('Choisissez une action:').strip()
    if choix == '1':
        pass
    elif choix == '2':
        pass
    elif choix == '3':
        pass
    elif choix == '4':
        pass
    elif choix == '5':
        pass
    elif choix == '6':
        pass
    elif choix == '7':
        pass
    elif choix == '8':
        pass
    elif choix == '9':
        pass
    else:
        choix = input('Choix erroné!  Re-entrez:')
