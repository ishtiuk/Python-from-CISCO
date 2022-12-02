
# NOTE: this program checks whether the classes are subclass of each other ;)

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:

    print(f"{cls1.__name__}:".ljust(17), end='')
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end='\t')
    print()



# NOTE: There is one important observation to make: each class is considered to be a subclass of itself.


# NOTE: Output: 
'''Vehicle:         True   False   False
   LandVehicle:     True   True    False
   TrackedVehicle:  True   True    True'''