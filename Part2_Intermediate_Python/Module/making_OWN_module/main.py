#!/usr/bin/env python3 

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))


import sys

for i in sys.path:
    print(i)