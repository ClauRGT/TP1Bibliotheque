def afficher_menu(n=50):
    for i in range(n):
        print('*', end='')
    print('')
    print("* Bienvenue dans la Bibliothèque < Lu_Ly_Cla >   *")
    print("* Choisissez l'une des options suivantes :       *")
    for i in range(n):
        print('*', end='')
    print('')
    print("* 1   Ajouter Adhérent                           *\n"
          "* 2   Supprimer Adhérent                         *\n"
          "* 3   Afficher les Adhérents                     *\n"
          "* 4   Ajouter Document                           *\n"
          "* 5   Supprimer Document                         *\n"
          "* 6   Afficher les Documents                     *\n"
          "* 7   Ajouter Emprunts                           *\n"
          "* 8   Retour d'un Emprunt                        *\n"
          "* 9   Afficher les Emprunts                      *\n"
          "* Q   Quitter                                    *"
          )

    for i in range(n):
        print('*', end='')
    print('')
afficher_menu()






