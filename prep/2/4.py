'''
Write a generator without_repetitions(it).
The it parameter is any iterable object.
The returned iterator contains it elements, excluding repetitions (i.e. those that have already occurred).

If it is empty, the returned iterator is also empty.
'''
def without_repetitions(it):
    seen = set()
    for i in it:
        if i not in seen:
            seen.add(i)
            yield i
    


g = without_repetitions([])
assert list(g) == []

g = without_repetitions('abc')
assert list(g) == list('abc')

g = without_repetitions('abcb')
assert list(g) == list('abc')

g = without_repetitions('aabdcb')
assert list(g) == list('abdc')


import random

random.seed(123)

def dice_rolls():
    while True:
        yield random.randint(1, 6)

lst = dice_rolls()
g = without_repetitions(lst)
assert sorted(next(g) for _ in range(6)) == [1, 2, 3, 4, 5, 6]