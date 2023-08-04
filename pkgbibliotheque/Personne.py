class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __str__(self):
        return "[Personne: " + self.nom + " " + self.prenom + "]"

class Adherent(Personne):
    def __init__(self, personne, num_adherent):
        super().__init__(personne.nom, personne.prenom, personne.age)
        self.num_adherent = num_adherent

    def __str__(self):
        return "Adherent| Nom: " + self.nom + " " + self.prenom + "Numéro d'adhérent: " + self.num_adherent


class Employe(Personne):
    def __init__(self, personne, num_employe):
        super().__init__(personne.nom, personne.prenom, personne.age)
        self.num_employe = num_employe

    def __str__(self):
        return "Employé| Nom: " + self.nom + " " + self.prenom + "Numéro d'employé: " + self.num_employe
