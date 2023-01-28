'''
Write a function filtered_sum(seq, pred), where

seq - sequence of numbers;
pred - one-parameter function.
filtered_sum(seq, pred) returns the sum of those values in seq where pred evaluates to True.
If pred evaluates to False on all values in seq, this call returns 0.
'''

def filtered_sum(seq, pred):
    total = 0
    for number in seq:
        if pred(number):
            total += number
    return total


seq = [-3, 1, 5, -4, 10]
pred1 = lambda x: x > 0
pred2 = lambda x: x % 2 == 0
pred3 = lambda x: True
pred4 = lambda x: False
assert filtered_sum(seq, pred1) == 16
assert filtered_sum(seq, pred2) == 6
assert filtered_sum(seq, pred3) == 9
assert filtered_sum(seq, pred4) == 0