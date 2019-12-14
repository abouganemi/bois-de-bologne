

while True:
    user_input = input("Entrez une valeur: ")
    user_input = int(user_input)
    if user_input < 0:
        print("Numero negative, adieu")
        break

    number = user_input % 2

    if number == 0:
        print("{} est un numero paire".format(user_input))
    else:
        print("{} est un numero impaire".format(user_input))