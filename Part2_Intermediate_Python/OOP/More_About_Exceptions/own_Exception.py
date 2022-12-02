
class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise MyZeroDivisionError("some bad news")


for mode in (True, False):
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print("division by zero")


for mode in (True, False):
    try:
        do_the_division(mode)
    except MyZeroDivisionError as myerr:
        print("my zerodivision error:", myerr.args)
    except ZeroDivisionError as ori_zr_err:
        print("orginal zerodivision error:", ori_zr_err)