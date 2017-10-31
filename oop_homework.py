# Part 1
class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    
    def distance(self):
        # ((x1+x2)**2 + (y1 + y2)**2)**0.5
        print(((coor1[0] + coor1[1])**2 + (coor2[0] + coor2[1])**2)**(0.5))
    
    def slope(self):
        # y2 - y1 / x2 - x1
        if (coor1[1] - coor1[0]) == 0:
            print('has no slope')
        else:
            print((coor2[1] - coor2[0])/(coor1[1] - coor1[0]))
            
"""
*** His solution ***
class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ( (x2-x1)**2 + (y2-y1)**2 )**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return float((y2-y1))/(x2-x1)
"""
    
#######################################################
# Part 2
class Cylinder(object):
    
    pi = 3.1459
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        # v= pi * r**2 * h
        print(Cylinder.pi*self.height+(self.radius**2))
    
    def surface_area(self):
        #A = (2 * pi * r * h) + (2 * pi * r**2)
        print((2*Cylinder.pi*self.radius*self.height)+(2*Cylinder.pi*(self.radius**2)))

"""
*** His Solution ***
class Cylinder(object):
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height * (3.14)* (self.radius)**2
    
    def surface_area(self):
        top = (3.14)* (self.radius)**2
        return 2*top + 2*3.14*self.radius*self.height
"""