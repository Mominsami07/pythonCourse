"""
Write the function is_int_geom(seq). The parameter seq is a sequence of integers.
The function returns True when seq has less than 2 elements or when there is an integer q such that for any two consecutive values in seq,
the next is the product of the preceding and q;
otherwise, the function returns False.

"""

def is_int_geom(seq):
    if len(seq) < 2:
        return True
    q = seq[1]/seq[0]
    for i in range(len(seq)-1):
        if int(seq[i+1])/int(seq[i]) != int(q):
            return False
    return True


assert is_int_geom([])
assert is_int_geom([3])
assert is_int_geom([7, 21])                  ## q = 3
assert is_int_geom([1, -1, 1, -1, 1, -1, 1]) ## q = -1
assert is_int_geom([6, 6, 6, 6])             ## q = 1
assert is_int_geom([2, 10, 50, 250, 1250])   ## q = 5 

assert not is_int_geom([7, 22])
assert not is_int_geom([1, 2, 4, 8, 15])
assert not is_int_geom([1, 2, 4, 9, 18])
assert not is_int_geom([1, 2, 5, 11])
assert not is_int_geom([9, 12, 16])