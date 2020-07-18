# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
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

class Vehicle():
    # BASE class which all subclasses will inherit from
    pass


class GroundVehicle(Vehicle):
    pass
    # class inherits from Vehicle


class FlightVehicle(Vehicle):
    pass
    # class inherits from vehicle


class Car(GroundVehicle):
    pass
    # class inherits from ground vehicle -> vehicle


class Motorcycle(GroundVehicle):
    pass
    # class inherits from ground vehicle-> vehicle


class Airplane(FlightVehicle):
    pass
    # class inherits from flight vehicle->vehicle


class Starship(FlightVehicle):
    pass
    # class inherits from flight vehicle->vehicle
