def premier(msg):
    print(msg)


premier("Bonjour")

second = premier

second("Bonjours")

print("#############"*3)


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def faire(fonc, x):
    result = fonc(x)
    return result


print(faire(inc, 3))
print(faire(dec, 3))
print("#############"*3)


def est_appele():
    def est_retourne():
        print("Bonjoursss")
    return est_retourne


nouveau = est_appele()
nouveau()
print("#############"*3)


def rendre_beau(fonc):
    def interne():
        print("J'ai ete decore")
        fonc()
    return interne


def ordinaire():
    print("Je suis ordinaire")


ordinaire()
beau = rendre_beau(ordinaire)
beau()

print("#############"*3)


def rendre_beau2(fonc):
    def interne2():
        print("J'ai ete decore 2")
        fonc()
    return interne2


@ rendre_beau2
def ordinaire2():
    print("Je suis ordinaire 2")


ordinaire2()
print("#############"*3)


def diviser_intelligent(fonc):
    def interne(a, b):
        print("Je vais diviser", a, "sur", b)
        if b == 0:
            print("Whoops!, tu peux pas")
            return
        return fonc(a, b)
    return interne


@diviser_intelligent
def diviser(a, b):
    return a / b


print(diviser(2, 5))
print(diviser(2, 0))
print("#############" * 3)


def etoile(fonc):
    def interne(msg):
        print("*" * 30)
        fonc(msg)
        print("*" * 30)
    return interne


def pourcentage(fonc):
    def interne(msg):
        print("%" * 30)
        fonc(msg)
        print("%" * 30)
    return interne


@etoile
@pourcentage
def imprimer(msg):
    print(msg)


imprimer("Hola")
