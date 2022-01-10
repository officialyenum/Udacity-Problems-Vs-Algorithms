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
    if number < 0:
        return None
    square_root = floor_number(number ** 0.5)
    return square_root

def floor_number(number):
    return int(number // 1)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt(-5)) else "Fail")