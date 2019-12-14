class Property:
    """ Class that will define a generic room characterized by :
    - Address
    - Rooms
    - Bathrooms
    - Description
    - Taxes """

    taxes = "$1000"

    def __init__(self, address, rooms, bathrooms, description):
        self.address = address
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.description = description

    def toString(self):
        print("Address: " + self.address + "\n" +
              "Rooms: " + self.rooms + "\n" +
              "Bathrooms: " + self.bathrooms + "\n" +
              "Description: " + self.description + "\n" +
              "Taxes: " + Property.taxes)

class Condo(Property):
    """ Class that will define a specific type of Formation characterized by:
    - Co-property fees """

    def __init__(self, address, rooms, bathrooms, description, fees):
        Property.__init__(self, address, rooms, bathrooms, description)
        self.fees = fees

    def toString(self):
        Property.toString(self)
        print("Fees: " + str(self.fees))

prop1 = Property("La luna", "3", "1", "Nice")
prop1.toString()

print("\n" + "//////////////////////////" + "\n")

condo = Condo("La luna", "3", "1", "Nice", 2500)
condo.toString()



