def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if(len(ints) == 0):
        # print('min_value : {} max_value : {}'.format(ints[0], ints[0]))
        return (0, 0)

    if(len(ints) == 1):
        # print('min_value : {} max_value : {}'.format(ints[0], ints[0]))
        return (ints[0], ints[0])

    if(len(ints) == 2):
        if(ints[0] > ints[1]):
            # print('min_value : {} max_value : {}'.format(ints[1], ints[0]))
            return (ints[1], ints[0])
        else:
            # print('min_value : {} max_value : {}'.format(ints[0], ints[1]))
            return (ints[0], ints[1])


    min_value = ints[0]
    max_value = ints[len(ints)-1]
    for value in ints:
        # print('min_value : {} max_value : {}'.format(min_value, max_value))
        if value <= min_value:
            min_value = value
        if value > max_value:
            max_value = value
    return (min_value, max_value)

## Example Test Case of Ten Integers
import random

# Test 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# Test 2
j = [i for i in range(-30, -10)]  # a list containing negative values
random.shuffle(j)

print ("Pass" if ((-30, -11) == get_min_max(j)) else "Fail")

# Test 3
j = [i for i in range(-10, -30)]  # a list containing negative values
random.shuffle(j)

print ("Pass" if ((0, 0) == get_min_max(j)) else "Fail")


# Test 4
k = [i for i in range(0, 1)]  # a list containing one value
random.shuffle(k)

print ("Pass" if ((0, 0) == get_min_max(k)) else "Fail")

# Test 5
l = [i for i in range(0, 2)]  # a list containing two values
random.shuffle(l)

print ("Pass" if ((0, 1) == get_min_max(l)) else "Fail")

# Test 6
h = []  # a list containing no values
random.shuffle(h)

print ("Pass" if ((0, 0) == get_min_max(h)) else "Fail")