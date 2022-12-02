
def print_exception_args(args):
    if len(args) == 0:
        print("")
    elif len(args) == 1:
        print(args[0])
    else:
        print(args)


try:
    raise Exception()
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print(e.args)


try: 
    raise Exception("My Exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print(e.args)


try:
    raise Exception("My", "Exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print(e.args)