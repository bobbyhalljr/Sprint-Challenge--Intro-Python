# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle:
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels

    # drive method
    def drive(self):
        print('Vrooooom!')


# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

# Subclass Motorcycle from GroundVehicle.
class Motorcycle(GroundVehicle):
    def __init_subclass__(cls, **kwargs):
        super.__init_subclass__(**kwargs)

    def __str__(self):
        return f"{self.num_wheels}"

    def drive(self):
        print('BRRAAAPPP!')

motorcycle = Motorcycle(num_wheels=2)
print(motorcycle)
print(motorcycle.drive())


vehicles = [
    GroundVehicle(num_wheels=4),
    GroundVehicle(num_wheels=4),
    Motorcycle(num_wheels=2),
    GroundVehicle(num_wheels=4),
    Motorcycle(num_wheels=2),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO

# awnser
for d in vehicles:
    print(d.drive())
