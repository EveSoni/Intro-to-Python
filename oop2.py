class cars:
    def __init__(self, model, make, year, colour):
        self.model=model
        self.make=make
        self.year=year
        self.colour=colour
    def display(self):
        print(f"My dream car is {self.model}, {self.make}, introduced in the year {self.year}, "
              f"and will be {self.colour} in colour")
myobj=cars("Toyoya", "Auris", 2006, "red")
myobj.display()

myobj2=cars("Mercedes", "GLS", 2015, "brown")
myobj.display()

myobj3=cars("Volkswagen", "Atlas", 2018, "grey")
myobj3.display()

myobj4=cars("BMW", "X7", 2021, "black")
myobj4.display()

# Inheritance - accessing properties from the parent class
class toyota(cars):
    def display(self):
        print(f"My dream car is {self.model}, {self.make}, introduced in the year {self.year}, "
              f"and will be {self.colour} in colour")
myobj=toyota("toyota", "premio", 2007, "white")
myobj.display()
