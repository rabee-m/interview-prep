#Cracking The Coding Interview pg 91 1.8

"""
Prompt:Write an algorithm such that if an element in a MxN matrix is 0, it's
entire row and column are set to 0
"""
from collections import defaultdict


def zero_matrix1(matrix):
    """
        Time Complexity: O(m*n), loop through each element
        Space Complexity: O(m + n), dictinoarys storing zero rows and cols
    """
    zero_rows = defaultdict(bool)
    zero_cols = defaultdict(bool)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_rows[i] = True
                zero_cols[j] = True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if zero_rows[i] or zero_cols[j]:
                matrix[i][j] = 0
    
    return matrix

def nullifyRow(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def nullifyCol(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

"""
O(1) Strategy:
We use the first row and first col to store which rows and columns we are zeroing out
instead of creating a dictionary
1. Check if first column or row have any zeros if they do, we handle edge case of
nullifying them at the end
2. Iterate through the matrix, setting matrix[i][0] and matrix[j][0] to zero, whenever
there's a zero in matrix[i][j]
3. Iterrate through entire matrix, and whenever we find value with matrix[i][0] == 0 or 
matrix[0][j] == 0, we nullify columns and rows
4. Handle the edge case of nuliifying first row and column if necessary
"""


def zero_matrix2(matrix):
    """
        Time Complexity: O(m*n), loop through each element in array
        Space Complexity: O(1) 
    """
    #check if first row and column have zeros
    firstRowHasZero = False
    firstColHasZero = False
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            firstRowHasZero = True
            break
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            firstColHasZero = True
            break
    
    #loop through the matrix and check what values are zero
    # when we find zero value set appropriate value to zero in the
    #first column and first row 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    #loop through first row and determine which columns to nullify
    #NOTE: we skip first value since we handle that later
    for i in range(1, len(matrix[0])):
        if matrix[0][i] == 0:
            nullifyCol(matrix, i)
    
    #loop through first col and determine which rows to nullify
    #NOTE: We skip first value since we handle that later
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullifyRow(matrix, i)
    
    #handle edge case of whether first row or column have to be nullified
    if firstRowHasZero:
        nullifyRow(matrix, 0)
    if firstColHasZero:
        nullifyCol(matrix, 0)

    return matrix


matrix = [[1, 0, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 0, 12]]

print(zero_matrix2(matrix))
