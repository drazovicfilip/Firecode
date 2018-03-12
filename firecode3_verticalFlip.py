""" You are given an m x n 2D image matrix (List of Lists) where each integer represents a pixel. Flip it in-place along its vertical axis.

Example:
Input image :
1 0              
1 0

Modified to :
0 1              
0 1 """

def flip_vertical_axis(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Traverse all rows
    for col in range(0, int(cols/2)):
        
        # Traverse all columns
        for row in range(0, rows):
        
            # Flip vertically mirrored indexes
            temp = matrix[row][col]
            matrix[row][col] = matrix[row][cols-1-col]
            matrix[row][cols-1-col] = temp 