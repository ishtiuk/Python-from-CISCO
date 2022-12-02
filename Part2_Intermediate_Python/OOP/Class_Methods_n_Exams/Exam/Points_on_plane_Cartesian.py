
import math            # not needed for me ;D


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        w_x = self.__x - x
        h_y = self.__y - y 
        hypo_oti = (w_x ** 2 + h_y ** 2) ** 0.5
        
        return hypo_oti

    def distance_from_point(self, point):
        w_x = self.__x - point.getx()          # this is 'width' in trigonometry, and 'x' axis in ML & statistics, that's why var name used as 'w_x'
        h_y = self.__y - point.gety()          # this is 'height' in trigonometry, and 'y' axis in ML & statistics, that's why var name used as 'h_y'
        
        hypo_oti = (w_x ** 2 + h_y ** 2) ** 0.5     # squre root ;)
        
        return hypo_oti
       

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
# print(point2.distance_from_xy(2, 0))
