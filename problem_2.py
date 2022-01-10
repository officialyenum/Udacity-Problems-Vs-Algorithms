def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    n = len(input_list)
    pivot_index = findPivot(input_list, 0, n-1) # find pivot used in rotating array, reverse engineering quicksort algorithm
    # If we didn't find a pivot, 
    # then array is not rotated at all
    if pivot_index == -1:
        return binary_search_recursive(input_list, 0, n-1, number)

    # If we found a pivot, then first
    # compare with pivot and then
    # search in two subarrays around pivot
    if input_list[pivot_index] == number:
        return pivot_index
    if input_list[0] <= number:
        return binary_search_recursive(input_list, 0, pivot_index-1, number)
    return binary_search_recursive(input_list, pivot_index + 1, n-1, number)


def findPivot(arr, start_index, end_index):
    # base cases
    # if end index is less than start index return -1 as pivot
    if end_index < start_index:
        return -1
    if end_index == start_index: # if end index is equal to start index return start index as pivot
        return start_index
    
    mid_index = (start_index + end_index)//2 # Get mid index of start and end index
    
    if mid_index < end_index and arr[mid_index] > arr[mid_index + 1]:
        return mid_index
    if mid_index > start_index and arr[mid_index] < arr[mid_index - 1]:
        return (mid_index-1)
    if arr[start_index] >= arr[mid_index]:
        # recurse from start to mid if value in array start index is >= value in array mid index
        return findPivot(arr, start_index, mid_index-1)
    # recurse mid + 1 index to end if no condition was met above
    return findPivot(arr, mid_index + 1, end_index)

# Using Binary Search Recursive Function
def binary_search_recursive(array, start_index, end_index, target):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]
    
    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive(array, start_index, mid_index - 1, target)
    else:
        return binary_search_recursive(array, mid_index + 1, end_index, target)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    # print(linear_search(input_list, number))
    # print(rotated_array_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test Case 1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Test Case 2
test_function([[], -1])

# Test Case 3
test_function([[2,3,4,5,6,-3,-2,-1,0,1], -2])