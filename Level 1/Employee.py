# -*- coding: UTF-8 -*-
class Employe:
    """ Classe definissant un employe caracterisee par :
    - son nom
    - son prenom
    - sa province de residente """
    age_retraite = 60
    object_crees = 0

    def __init__(self, nom, prenom): # Notre methode constrectueur

        self.nom = nom
        self.prenom = prenom
        self.matricule = 33
        self.province = "Quebec"
        self.note = ""

        Employe.object_crees += 1

    def ecrire(self, note_a_ecrire):
        if self.note != "":
            self.note += "\n"
        self.note += note_a_ecrire

    def lire(self):
        print(self.note)

    def effacer(self):
        self.note = ""

    @classmethod # this is a class method not an object method
    def combien(cls):
        print("Jusqu'a present, {} objects ont ete cress."
              .format(cls.object_crees))


employe1 = Employe("Isaac", "Abouganem")
print("Valor original - ", employe1.matricule, employe1.nom, employe1.prenom, employe1.province, employe1.note)

employe1.province = "Ontario"
print("L employe est - ", employe1.matricule, employe1.nom, employe1.prenom, employe1.province)

employe2 = Employe("Canelo", "Cortez-Abouganem")
print("L employe est - ", employe2.matricule, employe2.nom, employe2.prenom, employe2.province)


print(employe1.note)

print("//////////////////////////")
employe1.ecrire("recrutement")
employe1.lire()

print("//////////////////////////")
employe1.ecrire("Augmentation salaire")
employe1.lire()

print("//////////////////////////")
employe1.ecrire("Changement de poste")
employe1.lire()

print("//////////////////////////")
employe1.effacer()

print("//////////////////////////")
employe1.lire()

print("//////////////////////////")
employe1.ecrire("Augmentation salaire 3%")

print("//////////////////////////")
Employe.combien()
print("//////////////////////////")

class Stagiaire(Employe):
    """ Classe definissant un stagiare
    une specialisation d employee caracterisee par :
    - sa duree de stage de residence """

    def __init__(self, nom, prenom, duree_stage):
        Employe.__init__(self, nom, prenom)
        self.duree_stage = duree_stage

stagiare = Stagiaire("Rose", "Pasca", 45)
print(stagiare.duree_stage)
print("//////////////////////////")
print(stagiare.age_retraite)
print("//////////////////////////")
print(stagiare.province)
print("//////////////////////////")
stagiare.ecrire("Recrutement Stagiare")
stagiare.lire()