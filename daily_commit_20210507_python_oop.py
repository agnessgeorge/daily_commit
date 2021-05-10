# Object Oriented Programming

#### Problem 1
#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    
    def distance(self):
        print float((abs(self.coor1[0] - self.coor2[0]))**2 + (abs(self.coor1[1]-self.coor2[1]))**2)**0.5
        
        
    def slope(self):
        print float(self.coor2[1] - self.coor1[1])/float(self.coor2[0] - self.coor1[0])

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()

li.slope()

# Fill in the class
class Cylinder:

    from math import pi
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        print self.pi * (self.radius)**2 * self.height
    
    def surface_area(self):
        print 2 * self.pi * self.radius * (self.radius + self.height)

# EXAMPLE OUTPUT
c = Cylinder(2,3)

c.volume()

c.surface_area()