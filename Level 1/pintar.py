user_input = int(input("Entrez une valeur: "))

print("**************Premier cas**************")

for filas in range(0, user_input):
    for columnas in range(0, user_input):
        print("*", " ", end="")
        if columnas == user_input - 1:
            print("\n")

print("\n\n**************Deuxieme cas**************")

for filas in range(1, user_input + 1):
    for columnas in range(filas):
        print("*", " ", end="")
    print("\n")

print("\n\n**************Troizeme cas**************")

for filas in range(user_input):
    for columnas in range(user_input - filas):
        print("*", " ", end="")
    print("\n")
