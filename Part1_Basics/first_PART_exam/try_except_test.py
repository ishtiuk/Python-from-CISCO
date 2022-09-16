
try:
    a = input("enter number: ")
    print(5 / a)

except(ZeroDivisionError, TypeError, ZeroDivisionError) as err:
    print("ops err", err)
