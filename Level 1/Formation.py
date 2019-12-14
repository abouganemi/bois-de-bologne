class Formation:
    """ Class that will define a generic room characterized by :
    - Title
    - Duration in months
    - Type
    - Specialization
    - Credits """

    credits = 45

    def __init__(self, title, duration, type, specialization):
        self.title = title
        self.duration = duration
        self.type = type
        self.specialization = specialization

    def toString(self):
        print("Title: " + self.title + "\n" +
              "Duration: " + str(self.duration) + "\n" +
              "Type: " + self.type + "\n" +
              "Specialization: " + self.specialization + "\n" +
              "Credits: " + str(Formation.credits))

class Certification(Formation):
    """ Class that will define a specific type of Formation characterized by:
    - Co-property fees """

    def __init__(self, title, duration, type, specialization, institution):
        Formation.__init__(self, title, duration, type, specialization)
        self.institution = institution

    def toString(self):
        Formation.toString(self)
        print("Institution: " + str(self.institution))

network1 = Formation("CNNA", 2, "Basic", "Network")
network1.toString()

print("\n" + "//////////////////////////" + "\n")

vmware = Certification("AWS Architect", 1, "Advanced", "Virtualization", "ClouDa")
vmware.toString()



