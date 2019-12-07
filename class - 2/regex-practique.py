import re


def verifier(patron, chaine):
    result = re.match(patron, chaine)
    if result:
        print("Recherche réussie.")
    else:
        print("Recherche infructueuse.")


#Les crochets spécifient un ensemble de caractères
# que vous souhaitez faire correspondre.
verifier("[abc]", "abyss")
#Vous pouvez également spécifier une plage de caractères
# en utilisant - entre crochets.
verifier("[a-e]", "abyss")
verifier("[1-4]", "abyss")
#Vous pouvez inverser (complément) le jeu de caractères
# en utilisant le symbole ^ au début d'un crochet.
verifier("[^abc]", "abyss")
verifier("[^0-9]", "abyss")
#Le symbole ^ est utilisé aussi pour vérifier
# si une chaîne commence par un certain caractère.
verifier("^a", "abyss")
#Le symbole $ est utilisé pour vérifier
#si une chaîne se termine par un certain caractère.
verifier("a$", "abyss")
#Barre verticale | est utilisé pour l'alternance
# (opérateur ou).
verifier("a|b", "abyss")
#Les parenthèses () permettent de regrouper des sous-modèles.
# Par exemple, (a|b|c)xz correspond à n'importe
# quelle chaîne correspondant à a ou b ou c suivie de xz
verifier("(a|b|c)xz", "abyss")
#\A - Correspond si les caractères spécifiés
# sont au début d'une chaîne.
verifier("\Athe", "abyss")
#\b - Correspond si les caractères spécifiés
# sont au début ou à la fin d'un mot.
verifier(r"\bthe", "theabcd")
#\B - Opposé à \b . Correspond si les caractères
# spécifiés ne sont pas au début ou à la fin d'un mot.
verifier("\Bthe", "abythess")
#\d - Correspond à n'importe quel chiffre décimal.
# Équivalent à [0-9]
verifier("\d", "abyss")
#\D - Correspond à tout chiffre non décimal.
# Équivalent à [^0-9]
verifier("\D", "abyss")
#\w - Correspond à tout caractère alphanumérique
# (chiffres et alphabets). Équivalent à [a-zA-Z0-9_] .
verifier("\w", "****")
#\W - Correspond à tout caractère non alphanumérique.
# Équivalent à [^a-zA-Z0-9_]
verifier("\W", "abyss")
#\Z - Correspond si les caractères spécifiés
# sont à la fin d'une chaîne.' \
verifier("^.*Python\Z", "bonjour Python")
#Le symbole . remplace uncaractere
verifier("^b..n$", "bonjour python")
verifier("^p....n$", "python")
#Le symbole .* remplace 0 a n caracteres
verifier("^b.*n$", "bonjour python")
verifier("^b.*n$", "bn")
#Le symbole .+ remplace 1 a n caracteres
verifier("^b.+n$", "bonjour python")
verifier("^b.+n$", "bn")
