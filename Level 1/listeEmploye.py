listeNom=["Isaac", "Cristal", "Canelo", "Dupon", "Tobias"]
listSalaire=[2220, 2344.55, 1000000, 400]
listeEmploye = [listeNom, listSalaire]

newliste = []


for x in range(len(listeNom)):
    if x > len(listSalaire) - 1:
        newliste.append(listeNom[x] + " - " + "0")
    else:
        newliste.append(listeNom[x] + " - " + str(listSalaire[x]))
print(newliste)




