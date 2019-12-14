

listeNom=["Isaac", "Cristal", "Canelo", "Dupon"]
listSalaire=[2220, 2344.55, 1000000, 400]

print("La liste est:", listeNom)
print("Mon premier element est", listeNom[0])

listNom2=["Mr. Bean", "Max"]

listeNom3=listeNom + listNom2

print(listeNom3)

listeMixte= listeNom + listSalaire
print(listeMixte)

print("\n{} Gana {} pepitas... Cheeeeem !\n".format(listeNom[2], listSalaire[2]))


for x in range(len(listeNom)):
    print(listeNom[x])

print("\n************")

for y in range(len(listSalaire)):
    doubleSalaire = listSalaire[y] * 2
    print(doubleSalaire)

print("\n************")

listeNom4 = listeNom * 3
print(listeNom4)

print("\n************")

listeNom[0] = "Papo"
print(listeNom)

print("\n************")

if len(listeNom) == len(listSalaire):
    for x in range(len(listeNom)):
        print("El salario de {} es {:.2f}".format(listeNom[x], listSalaire[x]))
else:
    print("No son iguales")

print("\n************")

listeNom.append("Max")
print(listeNom)

print("\n************")

listeNom.insert(2, "Maria")
print(listeNom)

print("\n************")

listeNom.remove("Max")
print(listeNom)

print("\n************")

del listeNom[2]
print(listeNom)

print("\n************")

listeEmploye = [listeNom, listSalaire]
print(listeEmploye)
print(listeEmploye[1][1])

print("\n ************")

for x in range(len(listeEmploye)):
    for y in range(len(listeEmploye[x])):
        print(listeEmploye[x][y])

print("\n************")

for element in listeNom:
    print(element)

print("\n************")

listeVide=[]
print(listeVide)
listeVide.append("Isaac")
print(listeVide)

print("\n************")

nom = listeNom
print(nom[-2])

print("\n************")
existe = "Cristal" in listeNom
print(existe)

print("\n************")

if "Canelo" in listeNom:
    print("Yo choy un petioti")
else:
    print("Doch, Jechus, el vestido de manimani")

print("\n************")
position = listeNom.index("Canelo")
print(position)

print("\n************")
listeNom.append("Jean")
listeNom.reverse()
position = listeNom.index("Jean")
print(position)

print("\n************")
print(max(listSalaire))
print(min(listSalaire))

print("\n************")
def add_number(val1 , val2):
    resultat = val1 + val2
    return resultat

monResultat = add_number(5, 7)
print(monResultat)

print("\n************")
def afficher_nom(nom, prenom):
    print(nom + " - " + prenom)

afficher_nom("Isaac", "Abouganem")