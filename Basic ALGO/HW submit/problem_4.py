

import random


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    pivot = 1
    flag = 0
    next_small = 0
    next_large = len(input_list) -1
    while flag <= next_large:
        if input_list[flag] < pivot:
            swap(input_list, flag, next_small)
            next_small += 1
            flag += 1
        elif input_list[flag] > pivot:
            swap(input_list, flag, next_large)
            next_large -= 1
        else:
            flag += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")




def test_empty():
    test_function([])
    test_function([1])
    test_function([2])

def test_simple():
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

def test_random():
    test_case = []
    for i in range(0, 100):
        num = random.randint(0, 2)
        test_case.append(num)
    test_function(test_case)


test_empty()
test_simple()
test_random()