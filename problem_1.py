def sqrt(number):
    """
    Calculate the floored square root of a number
    Args:
        number(int): Number to find the floored squared root
    Returns:
        int: Floored Square Root
    """
    # Negative numbers don't have real square roots since a square is either positive or 0.
    # source : https://www.mathplanet.com/education/algebra-1/exploring-real-numbers/square-roots
    
    if number == None:#input is None
        return None
    if number <= 0:# return -1  if number is zero or negative
        return -1
    if number == 1:# return 1  if number is 1
        return 1

    # -----------Solution Test Start ----------

    # checker = 0
    # answer = number / 2 # n/2

    # # Iterate until checker is equal to answer
    # while(checker != answer):
    #     # store answer to new checker
    #     checker = answer
    #     # update new answer by using inital ((n / n/2) + n/2)/2
    #     answer = ((number / checker) + checker) //2
    # return answer
    
    # -----------Solution Test End -----------

    # ----- Solution Binary Search
    # to store floor of sqrt(number)
    result = 0
    # the square root of number cannot be more than n/2 for number > 1
    start = 1
    end = number // 2

    while start <= end:
        # find the mid between start and end
        mid = (start + end) // 2
        sqr = mid*mid
        # return mid if sqrt and number is a perfect square
        if sqr == number:
            return mid
        # if mid × mid is less than number
        elif sqr < number:
            # discard left search
            start = mid + 1
            # update result since we need a floor
            result = mid
        # if mid × mid is more than number
        else:
            # discard the right search 
            end = mid - 1
    return result
    # return result

    # ----- Solution Binary Search


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (-1 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (-1 == sqrt(-5)) else "Fail")