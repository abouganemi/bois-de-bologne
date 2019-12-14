class Equipment:
    """ Class that will define a generic equipment characterized by :
    - Name
    - Model
    - Receipt Number
    - Maker
    - Life time guarantee """

    life_time = 5

    def __init__(self, name, model, receipt, maker):
        self.name = name
        self.model = model
        self.receipt = receipt
        self.maker = maker

    def toString(self):
        print("Name: " + self.name + "\n" +
              "Model: " + self.model + "\n" +
              "Receipt: " + str(self.receipt) + "\n" +
              "Maker: " + self.maker + "\n" +
              "Life Time: " + str(Equipment.life_time) + " years" + "\n")

class Monitor(Equipment):
    """ Class that will define a monitor, which is a specific type of equipment caracterized by:
    - resolution """

    def __init__(self, name, model, receipt, maker, resolution):
        Equipment.__init__(self, name, model, receipt, maker)
        self.resolution = resolution

    def toString(self):
        Equipment.toString(self)
        print("Resolution: " + self.resolution)

pc = Equipment("Gaming 1", "R500", 1, "Fractal Desing")
pc.toString()

print("\n" + "//////////////////////////" + "\n")

monitor1 = Monitor("ROG", "G20", 2, "Asus", "2048 x 1992")
monitor1.toString()


