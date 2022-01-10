def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    midpoint = len(items) // 2
    left = items[:midpoint]
    right = items[midpoint:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1
    
    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]
        
    # return the ordered, merged list
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
        input_list(list): Input List
    Returns:
        (int),(int): Two maximum sums
    """
    leftSum = ""
    rightSum = ""
    n = len(input_list)
    if n == 0: # validate length of list
        return [ 0, 0]
    sorted_digits = mergesort(input_list) # get sorted digits using merge sort algorithm
    if(sorted_digits[n-1] > 9 or sorted_digits[0] < 0 ): # validate digit is range 0-9
        return [0, 0]
    for index in range(n - 1, -1, -1): # traverse from end of sorted digits to 0 index
        if index % 2 == 0:
            leftSum += str(sorted_digits[index])
        else:
            rightSum += str(sorted_digits[index])
    return [int(leftSum), int(rightSum)]
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test case 1
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Test case 2
test_function([[], [0, 0]])

# Test case 3
test_function([[-4, 6, 2, -5, 9, 8], [0, 0]])

# Test case 4
test_function([[55, 6, 2, 10, 9, 8], [0, 0]])