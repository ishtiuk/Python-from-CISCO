
import math             # not needed for me ;D


class Point:
    # The code copied from the previous lab.
    
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y
    

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__params = [vertice1, vertice2, vertice3]


    def perimeter(self):
        x = self.__params[0].getx() + self.__params[1].getx() + self.__params[2].getx()
        y = self.__params[0].gety() + self.__params[1].gety() + self.__params[2].gety() 
        hypo = (x ** 2 + y ** 2) ** 0.5
        
        perim = x + y + hypo
        
        return perim


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
