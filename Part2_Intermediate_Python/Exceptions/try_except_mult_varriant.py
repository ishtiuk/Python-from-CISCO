
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)

except ValueError:
    print("Oh dear, value must be integer..!")
except ZeroDivisionError:
    print("Oh dear, can't perform division by zero")
except KeyboardInterrupt:
    print("Oh dear, Program has been terminated from Keyboard..!")
except:
    print("Oh dear, something went wrong...")
    
print("THE END.")
