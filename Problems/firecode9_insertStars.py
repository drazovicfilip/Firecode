""" 
Given a string, recursively compute a new string 
where identical, adjacent characters 
get separated with a "*".  

Example:
insert_star_between_pairs("cac") ==> "cac"

insert_star_between_pairs("cc") ==> "c*c" 
"""

def insert_star_between_pairs(a_string):
    
    # Check for empty strings
    if a_string == None or a_string == "":
        return 

    # Iterate through the whole array, checking for duplicates
    for i in range(0, len(a_string)):

        # If the current letter is duplicated
        if a_string[i+1] == a_string[i]:

            # Insert a star in the string
            a_string = a_string[:i+1] + "*" + a_string[i+1:]
    
    return a_string

