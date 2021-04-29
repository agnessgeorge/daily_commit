class Shape(object):
    
    def __init__(self):
        pass

    def area(self):
        print ('0')


class Square(Shape):

    def __init__(self, length=1):
        self.length = length

    def area(self):
        print (self.length * self.length)


squareOne = Square(4)
squareOne.area()