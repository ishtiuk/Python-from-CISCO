
import math


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))




# more ways to 'import'

from math import sin, pi                 # specifically imports the entities or vars, funcs whatever as your requirement.
from math import *                       # imports all the stuffs/ entities.
import math as mth                       # renames the module name for the current code or script.

from sys import winver as winvr, exit as ex, argv as argus