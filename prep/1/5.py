'''
Write the class Interval. Class objects represent open intervals on the number line
(open means an empty interval and intervals that does not contain any of its ends). The class should have methods:

.__init__(self, a, b) - initializes the left (a) and right (b) end of the interval self. If b <= a, we interpret the self interval as empty.
.is_empty(self) - returns True if self is empty.
.nb(self, seq) - returns number of elements from the sequence of numbers seq that belong to the interval self.
'''

class Interval:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def is_empty(self):
        return self.a >= self.b
    
    def nb(self, seq):
        count = 0
        for number in seq:
            if self.a < number < self.b:
                count += 1
        return count


A = Interval(-20, 200)
B = Interval(10, 10)
C = Interval(30, 4)

assert not A.is_empty()
assert B.is_empty()
assert C.is_empty()
assert A.nb(range(-100, 1000, 50)) == 4 ## 0 50 100 150
assert B.nb([9, 10, 11]) == 0
assert C.nb(range(-100, 1000, 50)) == 0