
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
        input_list(list): List to be sorted
    """
    start_pos_0 = 0
    end_pos_2 = len(input_list) - 1

    front_index = 0
    count = 0

    if len(input_list) < 0:
        # no value detected in list
        return -1

    while front_index <= end_pos_2:
        count += 1 #for debugging to ensure the loop traverses just once
        if input_list[front_index] < 0 or input_list[front_index] > 2:
            # invalid number detected in the list 
            return -1
        if input_list[front_index] == 0:
            # move value in start position to front index 
            input_list[front_index] = input_list[start_pos_0]
            # add 0 to start position
            input_list[start_pos_0] = 0
            # increase start position so the next zero found in the array can be placed there
            start_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2:   
            # move value in end position to front index         
            input_list[front_index] = input_list[end_pos_2] 
            # add 2 to end position position
            input_list[end_pos_2] = 2
            # decrease end position so the next value can be placed there
            end_pos_2 -= 1
        else:
            # traverse to next front index
            front_index += 1
    # print(len(input_list) == count) Test to ensure traversal is a single traversal
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case) or sorted_array == -1:
        print("Pass")
    else:
        print("Fail")

# Test Case 1
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Test Case 2
test_function([])
# Test Case 3
test_function([5,5,5,-5,2,2,2,-1,1,1,1])