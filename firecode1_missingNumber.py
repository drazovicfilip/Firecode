""" Given an list containing 9 numbers ranging from 1 to 10, write a function to find the missing number. Assume you have 9 numbers between 1 to 10 and only one number is missing.

Example:
input_list: [1, 2, 4, 5, 6, 7, 8, 9, 10]
find_missing_number(input_list) => 3 """

def find_missing_number(list_numbers):
    
    # 1 + 2 + ... + 10 = 55
    expectedSum = 55;
    
    # Sum the numbers in the array 
    givenSum = 0;
    for i in range(0,9):
        givenSum = givenSum + list_numbers[i];
    
    # Compare with 55. The difference is the missing number
    return expectedSum - givenSum;