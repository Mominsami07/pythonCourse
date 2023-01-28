'''
Write the function apply(*args, key). The key parameter is a one-parameter function.
The apply() function returns a list of values returned by successive key calls on args elements.
If args is empty, then the returned list is also empty.
'''

def apply(*args, key):
    return [key(arg) for arg in args]

def f(x):
    return x

def h(x):
    return x + 10

def g(x):
    return x > 0

assert apply(2, 3, 4, key=f) == [2, 3, 4]
assert apply(2, 3, 4, key=h) == [12, 13, 14]
assert apply(-5, 1, -2, 0, key=g) == [False, True, False, False]

def uppercase(s):
    return s.upper()

assert apply('a', 'bc', key=uppercase) == ['A', 'BC']
assert apply(key=uppercase) == []