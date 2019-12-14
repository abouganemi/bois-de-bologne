class Vehicule:
    """ Class that will define a vehicle caracterized by :
    - Maker
    - Brand
    - Model
    - Plate number  """

    model_year = 2008

    def __init__(self, maker, brand, model, plate ):
        self.maker = maker
        self.brand = brand
        self.model = model
        self.plate = plate

    def toString(self):
        print("Car Maker: " + self.maker + "\n" +
              "Brand: " + self.brand + "\n" +
              "Model: " + self.model + "\n" +
              "Year: " + str(Vehicule.model_year) + "\n" +
              "License plate: " + self.plate)

class moto(Vehicule):
    """ Class that will define a moto which is a Vehicle specialization
    caracterized by:
    - power """

    def __init__(self, maker, brand, model, plate, power ):
        Vehicule.__init__(self, maker, brand, model, plate)
        self.power = power

    def toString(self):
        Vehicule.toString(self)
        print("Power: " + str(self.power))

car1 = Vehicule("Mercedez", "Class S", "S500", "R50-GGR")
car1.toString()

print("\n" + "//////////////////////////" + "\n")

moto1 = moto("Yamaha", "Ninja", "N700", "A90-PRD", 5000)
moto1.toString()


