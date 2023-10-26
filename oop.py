class fruits:
    # constructor
    def __init__(self, type, price, weight, shape):
        self.type=type
        self.price=price
        self.weight=weight
        self.shape=shape
        # method
    def display(self):
        print(f"I like eating {self.type}, it weighs {self.weight} grams"
              f",its shape is {self.shape} and costs {self.price} ksh")
        # objects
myobj=fruits("watermelon", 50, 450, "oval")
myobj.display()

myobj2=fruits("bananas", 100, 250, "curved")
myobj2.display()

myobj3=fruits("pineapples", 150, 500, "circular")
myobj3.display()