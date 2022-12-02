
class Vehichles:
    defination = "We all are the vehicles..."

class Land_Vehichles(Vehichles):
    own_defination = "We are the land vechicles"

    def working_area(self):
        print("We run on land")


class Water_Vehichles(Vehichles):
    own_defination = "We are the water vechicles"

    def working_area(self):
        print("We run on water")

class Air_Vehichles(Vehichles):
    own_defination = "We are the air vechicles"

    def working_area(self):
        print("We run on air")



class Wheeled_Vehichles(Land_Vehichles):
    specific_defination = "I'm a wheeled vechicle"

    def working_area(self):
        # return super().working_area()
        print("I run using my wheels")

class Hovercrafts(Land_Vehichles):
    specific_defination = "I'm a hovercraft vechicle"

    def working_area(self):
        # return super().working_area()
        print("I run using my pumped paddles")


print(Wheeled_Vehichles().working_area())
