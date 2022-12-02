

# NOTE: The "self" parameter is also used to invoke other object/class methods from inside the class.

class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()
        Classy.other(self)


obj = Classy()
obj.method()

