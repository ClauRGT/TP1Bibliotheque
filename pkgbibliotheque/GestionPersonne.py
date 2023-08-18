class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __str__(self):
        return "[Personne: " + self.nom + " " + self.prenom + "]"

    @staticmethod
    def lire_clavier():
        print("------- Saisir Personne -------")
        nom = input("Personne.nom: ")
        prenom = input("Personne.prenom : ")
        age = input("Personne.age: ")
        return Personne(nom, prenom, age)

class Adherent(Personne):
    def __init__(self, personne, num_adherent):
        super().__init__(personne.nom, personne.prenom, personne.age)
        self.num_adherent = num_adherent

    def __str__(self):
        return "Adherent| Nom: " + self.nom + " " + self.prenom + " Numéro d'adhérent: " + self.num_adherent

    @staticmethod
    def lire_clavier():
        print("------- Saisir Adherent -------")
        nom = input("Adherent.nom: ")
        prenom = input("Adherent.prenom : ")
        age = input("Adherent.age: ")
        num_adherent = input("Adherent.num_adherent: ")
        return Adherent(Personne(nom, prenom, age), num_adherent)

class Employe(Personne):
    def __init__(self, personne, num_employe):
        super().__init__(personne.nom, personne.prenom, personne.age)
        self.num_employe = num_employe

    def __str__(self):
        return "Employé| Nom: " + self.nom + " " + self.prenom + "Numéro d'employé: " + self.num_employe

    @staticmethod
    def lire_clavier():
        print("------- Saisir Employe -------")
        nom = input("Employe.nom: ")
        prenom = input("Employe.prenom : ")
        age = input("Employe.age: ")
        num_employe = input("Employe.num_employe: ")
        return Employe(Personne(nom, prenom, age), num_employe)