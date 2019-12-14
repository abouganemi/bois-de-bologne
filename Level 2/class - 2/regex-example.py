import re

chaine = "un exemple word:cat, word:dog!"


#La fonction match est utilisée pour rechercher des correspondances
# au début d'une chaîne uniquement.
correspondance = re.match("word:\w\w\w", chaine)

# La Déclaration IF après le match() teste si le match a réussi ou pas
if correspondance:
    print(correspondance)
    print(correspondance[0])
else:
     print("n'a pas trouvé")

#Cette fonction ressemble beaucoup à match, sauf qu’elle regarde
# toute la chaîne et retourne la première correspondance.
correspondance = re.search("word:\w\w\w", chaine)

if correspondance:
    print(correspondance.group())
    print(correspondance.start())
    print(correspondance.end())
else:
    print("n'a pas trouvé")
    
    
#Findall trouve toutes les occurrences d'un motif dans une chaîne. 
# Ceci diffère des deux fonctions précédentes en ce sens qu'il ne renvoie pas d'objet de correspondance. 
# Il retourne simplement une liste de correspondances.

correspondance = re.findall("word:\w\w\w", chaine)
if correspondance:
    print(correspondance)
    print(correspondance[0])
else:
    print("n'a pas trouvé")