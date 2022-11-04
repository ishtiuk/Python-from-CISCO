
def exception_tree_print(excep, nest=0):
    if nest > 1:
        print("    |" * (nest - 1), end='')
    if nest > 0:
        print("    +---", end='')
    


    print(excep.__name__)

    for cls in excep.__subclasses__():
        exception_tree_print(cls, nest + 1)


exception_tree_print(BaseException)
