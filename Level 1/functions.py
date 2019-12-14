import random


def add_numbers_list(maListe):
    resultat = 0
    for element in maListe:
        resultat += element
    return resultat


listEntier = [random.randint(0, 30),
              random.randint(0, 30),
              random.randint(0, 30),
              random.randint(0, 30),
              random.randint(0, 30)]

total = add_numbers_list(listEntier)
print(total)

print("\n************")


def count_even_number(maListe):
    resultat = 0
    evenNumber = 0
    for element in maListe:
        if element % 2 == 0:
            evenNumber += 1
    return evenNumber


print(listEntier)

print(count_even_number(listEntier))
