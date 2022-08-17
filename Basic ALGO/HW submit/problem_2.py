

def rotated_search(arr, number, start, end):
    #base case 1 array is empty
    if (start >= end):
        return -1
    # base case 2 there is only one element in the array
    if (end == start + 1):
        if arr[start] == number:
            return start
        else:
            return -1

    # divide    
    mid = (start + end) // 2
    if (arr[mid] == number) :
        return mid

    left_start = start
    left_end = mid
    right_start = mid
    right_end = end
    
    # if left is sorted
    if arr[left_end] > arr[left_start]:
        if arr[left_end] < number or arr[left_start] > number:
            # search in right
            return rotated_search(arr, number, right_start, right_end)
        else:
            # search in left
            return rotated_search(arr, number, left_start, left_end)
    else:
        if arr[right_end - 1] < number or arr[right_start] > number:
            return rotated_search(arr, number, left_start, left_end)
        else:
            return rotated_search(arr, number, right_start, right_end)
   



def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return rotated_search(input_list, number, 0, len(input_list))


   




def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


def test_sample():
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])

def test_empty():
    test_function([[], 1])
    test_function([[1], 1])
    test_function([[1], 2])

def test_sortedArray():
    test_function([[1, 2, 3, 4, 5, 6, 7], 6])
    test_function([[1, 2, 3, 4, 5, 6, 7], 7])
    test_function([[1, 2, 3, 4, 5, 6, 7], 1])
    test_function([[1, 2, 3, 4, 5, 6, 7], 10])
    
test_sample()
test_empty()
test_sortedArray()