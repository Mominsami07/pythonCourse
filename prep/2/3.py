'''
Write the function is_alternating(seq).
The seq parameter is a sequence of numbers.
The function returns True when seq is empty or when it alternates between positive and negative values.
Otherwise, the function returns False.
'''

def is_alternating(seq):
    if len(seq) == 0:
        return True
    sign = None
    for i in range(len(seq)):
        if seq[i] != 0:
            if sign is None:
                sign = (seq[i] > 0)
            elif (seq[i] > 0) == sign:
                return False
            else:
                sign = (seq[i] > 0)
        else:
            return False
    return True


assert is_alternating(())
assert is_alternating([3])
assert is_alternating([-90])
assert is_alternating([3, -2, 6, -1, 7])
assert is_alternating([-10, 3, -2, 6, -1, 7])

assert not is_alternating([3, -2, 6, 5, -1, 7])
assert not is_alternating([3, -2, 6, -1, -5, 7])
assert not is_alternating([0])
assert not is_alternating([1, -1, 0])
assert not is_alternating([-1, 1, 0])