""" You are given an m x n 2D image matrix (List of Lists) where each integer represents a pixel. Flip it in-place along its horizontal axis.

Example:

Input image :  
              1 1
              0 0
Modified to :   
              0 0
              1 1 """

def flip_horizontal_axis(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Traverse all rows
    for  row in range(0, int(rows/2)):
        
        # Traverse all columns
        for col in range(0, cols):
        
            temp = matrix[row][col]
            matrix[row][col] = matrix[rows-1-row][col]
            matrix[rows-1-row][col] = temp


            