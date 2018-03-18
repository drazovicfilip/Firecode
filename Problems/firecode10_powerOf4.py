"""
Write a method to determine whether a given integer (zero or positive number) is a power of 4 without using the multiply or divide operator. If it is, return True, else return False.

Examples:
is_power_of_four(5) ==> False

is_power_of_four(16) ==> True

An integer is considered to be a power of 4 if 
1) it is one or 
2) there is only one bit set in its binary representation 
and the number of bits to the right of the set bit is even.
"""

def is_power_of_four(number):
    
    if number == 1:
        return True
    
    # Check if there is only one bit set 
    setBit = 0
    for i in range(1, 16):
        if number >> i & 1:
            if setBit > 0:
                return False
            else:
                setBit = i

    if setBit%2 == 0:
        return True
    
    return False

print(is_power_of_four(2048))