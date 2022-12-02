
# NOTE: this program checks whether the objects are instance of above defined classes ;)
# Being an instance of a class means that the object (the cake) has been prepared using a recipe contained in either the class or one of its superclasses.

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


vehicle_obj = Vehicle()
landVehicle_obj = LandVehicle()
trackedVehicle = TrackedVehicle()


for obj in [vehicle_obj, landVehicle_obj, trackedVehicle]:
    
    for clss in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, clss), end='\t')
    print()



# NOTE: isinstance(objectName, ClassName)