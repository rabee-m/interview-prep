"""
Cracking The Coding Interview pg 91 1.7
1 1 1
2 2 2
3 3 3
[[1 1 1],
[2 2 2],
[3 3 3]]


3 2 1
3 2 1
3 2 1
[[3 2 1],
[3 2 1],
[3 2 1]]

Essentially bottom row becomes first column
            2nd last row becomes second column
"""
#Take value in (0, 0) -> (0, 2) -> (3, 2) -> (2, 0) -> (0, 0)
# Take value in (0 , 1) -> (1, 2) -> (2, 2) -> (1, 2) -> (0, 1)

def rotateMatrix(matrix):
    """
        Time Complexity: O(n^2), since we traverse each element in the n*n matrix
        Space Complexity: O(1)
    """
    l, r = 0, len(matrix) - 1 #pointers to left-most and right-most column

    while l < r:
    #each while loop repersents traversing a layer of the matrix and rotating it

        #iterrate through except we don't go to last val
        for i in range(l, r - 1): #range(r - l)

            top, bottom = l, r #since it's square matrix dim will be same

            #save the topleft
            topLeft = matrix[top][l + i]

            #move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i ][l]
            #move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]
            #move top right into bottom right 
            matrix[bottom][r - i] = matrix[top + i][r]
            #move topleft into top right
            matrix[top + i][r] = topLeft

        #go inside to the next inner square of matrix
        l += 1
        r -= 1
    return matrix