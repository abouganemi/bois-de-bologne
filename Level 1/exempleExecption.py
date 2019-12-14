valeur1 = 15
valeur2 = 0
valeur3 = "Isaac"
valeur4 = 3

try:
    print(valeur1 / valeur2)
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par Zero")
except TypeError:
    print("Vous ne pouvez par une chaine")
except:
    print("Vous avez une erreur inconue")
finally:
    print("au revoir")