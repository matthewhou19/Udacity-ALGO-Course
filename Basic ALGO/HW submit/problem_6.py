import random
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max = ints[0]
    min = ints[0]
    for num in ints:
        if max < num:
            max = num
        if min > num:
            min = num
    return (min, max)



## Example Test Case of Ten Integers



def test_one_element():
    l = [1]
    print ("Pass" if ((1, 1) == get_min_max(l)) else "Fail")

def test_simple():
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

def test_random():
    l= []
    for i in range(100):
        l.append(random.randint(0, 100))
    res = get_min_max(l)
    l.sort()
    print ("Pass" if ((l[0], l[len(l) - 1]) == res) else "Fail")



test_one_element()
test_simple()
test_random()