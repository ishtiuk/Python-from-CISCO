

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("    |" * (nest - 1), end='')
    if nest > 0:
        print("    +---", end='')

    print(thisclass.__name__)

    for subcls in thisclass.__subclasses__():
        print_exception_tree(subcls, nest + 1)


print_exception_tree(BaseException)
