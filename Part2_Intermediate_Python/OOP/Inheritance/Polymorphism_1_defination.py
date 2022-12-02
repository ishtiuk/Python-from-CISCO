
# NOTE: "the situation in which the subclass is able to modify its superclass behavior (just like in the example) is called polymorphism." 
# 
# The word comes from Greek (polys: "many, much" and morphe, "form, shape"), which means that one and the same class can take various forms 
# depending on the redefinitions done by any of its subclasses.


class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()
