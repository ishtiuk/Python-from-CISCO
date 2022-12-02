
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese



try:
    raise TooMuchCheeseError("chicken pizza", "too much", "too much cheese are given")
except TooMuchCheeseError as err:
    print(err, err.pizza, err.cheese, err.args, sep=' | ')