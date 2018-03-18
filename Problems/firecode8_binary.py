""" Write a function to compute the binary representation of a positive decimal integer. The method should return a string. 

Example:
dec_to_bin(6) ==> "110"

dec_to_bin(5) ==> "101"
Note : Do not use in-built bin() function. """

def dec_to_bin(number):
    
    binary = ""
    
    # Halve the number and append the remainder to the current binary number
    while number > 1:
        binary = binary + str(number%2)
        number = int(number/2)

    # Add an additional 1
    binary = binary + str(1)
    
    # Reverse the string
    return binary[::-1]    
