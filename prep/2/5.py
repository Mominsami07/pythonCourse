"""
Write a class Rectangle. Objects of this class correspond to rectangles with sides parallel to the axis of the coordinate system.
The class should contain methods:

.__init__(self, x0, y0, x1, y1) - initializes the coordinates of the lower left (x0, y0) and upper right (x1, y1) vertices of the rectangle.
You may assume that x0 <= x1 and y0 <= y1.
.area(self) - returns the area of the rectangle.
.vertices(self) - returns a list of coordinates (as two-element tuples) of the vertices of a rectangle:
first the lower left vertex, then the others counterclockwise.
"""

class Rectangle:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        
    def area(self):
        width = self.x1 - self.x0
        height = self.y1 - self.y0
        return width * height
    
    def vertices(self):
        return [(self.x0, self.y0), (self.x1, self.y0), (self.x1, self.y1), (self.x0, self.y1)]



P = Rectangle(0, 0, 6, 7)
assert P.area() == 42
assert P.vertices() == [(0, 0), (6, 0), (6, 7), (0, 7)]

P = Rectangle(-2, 0, 5, 6)
assert P.area() == 42
assert P.vertices() == [(-2, 0), (5, 0), (5, 6), (-2, 6)]


