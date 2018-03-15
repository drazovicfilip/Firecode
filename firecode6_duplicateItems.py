""" Write a function - duplicate_items to find the redundant or repeated items in a list and return them in sorted order. 
This method should return a list of redundant integers in ascending sorted order (as illustrated below). 

Examples:
duplicate_items([1, 3, 4, 2, 1]) => [1]

duplicate_items([1, 3, 4, 2, 1, 2, 4]) => [1, 2, 4] """

def duplicate_items(list_numbers):

    list_numbers.sort()
    dupes = []

    # Iterate through the whole array, checking for duplicates
    for i in range(0, len(list_numbers)-1):

        # If the current number is duplicated
        if list_numbers[i+1] == list_numbers[i]:
            
            # Store it
            temp = list_numbers[i]
            dupes.append(temp)
            i = i + 1

    # Remove duplicates
    return list(set(dupes))
