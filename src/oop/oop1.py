# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]

# base class 
class Vehicle:
    def __init__(self):
        pass

# base class
class Flight_vehicle:
    def __init__(self):
        pass

class Airplane(Flight_vehicle):
    def __inti__(self):
        super.__init__()
    pass

# base class
class Starship:
    def __init__(self):
        pass

class Ground_vehicle(Vehicle):
    def __init__(self):
        super.__init__()
    pass

class Car(Ground_vehicle):
    def __init__(self):
        super.__init__()
    pass

class Motorcycle(Ground_vehicle):
    def __init__(self):
        super.__init__()
    pass


#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

