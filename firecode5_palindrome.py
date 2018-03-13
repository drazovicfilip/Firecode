""" A palindrome is a string or sequence of characters that reads the same backward and forward. For example, "madam" is a palindrome.
Write a function that takes in a string and returns a Boolean -> True if the input string is a palindrome and False
if it is not. An empty string is considered a palindrome. You also need to account for the space character. For example, "race car" should return False as read backward it is "rac ecar".

Examples:
is_palindrome("madam") -> True

is_palindrome("aabb") -> False

is_palindrome("race car") -> False

is_palindrome("") -> True """

def is_palindrome(input_string):
    length = len(input_string)
    
    # Traverse through half of the string (ignoring the middle character if the length is odd)
    for i in range(0, int(length/2)):

        # If any character doesn't match the opposite part of the string
        if not input_string[i] == input_string[length-i-1]:
            return False
    
    return True

