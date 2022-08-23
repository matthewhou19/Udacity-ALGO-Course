"""
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
"""

def counting_sort(arr):
    counts = [0,0,0,0,0,0,0,0,0,0]
    for num in arr:
        counts[num] += counts[num] + 1
    start = 0
    for i in range(0, 10):
        for j in range(0, counts[i]):
            arr[start] = i
            start += 1
    

def rearrange_digits(input_list):
    
    counting_sort(input_list)
    largest = len(input_list) - 1
    left = 0
    right = 0
    next_is_left = True
    while largest > -1:
        if next_is_left:
            left = left * 10 + input_list[largest]
        else:
            right = right * 10 + input_list[largest]
        next_is_left = not next_is_left
        largest -= 1
    return [left, right]






def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")



def test_empty():
    test_function([[],[0, 0]])

def test_zero():
    test_function([[0], [0, 0]])
    test_function([[9], [9, 0]])
def test_simple():
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_case_1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
    test_case_2 = [[9, 8 ,0, 2, 1], [920, 81]]
    test_function(test_case_1)
    test_function(test_case_2)


test_empty()
test_zero()
test_simple()