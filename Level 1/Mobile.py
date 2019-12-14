class Mobile:
    """ Class that will define a generic mobile device characterized by :
    - Brand
    - Reference
    - Resolution
    - Hard Drive
    - RAM """

    ram = 8

    def __init__(self, brand, reference, resolution, hdd):
        self.brand = brand
        self.reference = reference
        self.resolution = resolution
        self.hdd = hdd

    def toString(self):
        print("Brand: " + self.brand + "\n" +
              "Reference: " + self.reference + "\n" +
              "Resolution: " + self.reference + "\n" +
              "HDD - Gib: " + self.hdd + "\n" +
              "RAM - GB: " + str(Mobile.ram))

class Tablet(Mobile):
    """ Class that will define a specific mobile device (Certification) characterized by:
    - battery life """

    def __init__(self, brand, reference, resolution, hdd, battery):
        Mobile.__init__(self, brand, reference, resolution, hdd)
        self.battery = battery

    def toString(self):
        Mobile.toString(self)
        print("Battery Life: " + self.battery)

mobile1 = Mobile("Samsung", "2IKDX", "512 x 384", "16")
mobile1.toString()

print("\n" + "//////////////////////////" + "\n")

tablet1 = Tablet("Apple", "IpadX", "1024 x 768", "32", "2 Days")
tablet1.toString()




