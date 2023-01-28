'''
Write a triples(it) generator function. The it parameter is any iterable object.
The returned generator contains overlapping tuples of consecutive triples of it.

If it has less than three elements, the returned generator is empty.
'''

def triples(it):
    # Convert the iterable object to a list
    it = list(it)

    # Check if the iterable object has less than three elements
    if len(it) < 3:
        # Return an empty generator
        return

    # Iterate through the list with a sliding window of size 3
    for i in range(len(it) - 2):
        yield (it[i], it[i+1], it[i+2])


g = triples('abcdef')
assert list(g) == [
    ('a', 'b', 'c'),
    ('b', 'c', 'd'),
    ('c', 'd', 'e'),
    ('d', 'e', 'f')
]

g = triples('')
assert list(g) == []

g = triples([1, 2, 3])
assert list(g) == [(1, 2, 3)]

g = triples([1, 2])
assert list(g) == []

g = triples([1])
assert list(g) == []

g = triples(iter('xyzu'))
assert next(g) == ('x', 'y', 'z')
assert next(g) == ('y', 'z', 'u')