#AlgoExpert Easy Problem: Sorted Squared Array

#Prompt: Given an input return a sorted value of squares. Note: negative numbers may be difficult

#Solution 1: Iterrate through the list once, and square each element, then sort the array
#Time: O(n*logn), due to sorting
#Space: O(1)
def sortedSquaredArray1(array):
    sortedSquares = [x ** 2 for x in array]
    sortedSquares.sort()
    return sortedSquares

#Solution 2: Intialize two pointers, one that points to the left most value in array, and one that points to 
#the right most value in the array. Then create an empty array, and fill it from the back. At each step compare,
#whether the right or left pointer gives the greater value, insert that value into output array at back, then read adjust pointers
#Time: O(n)
#Space: O(n), creating new array
def sortedSquaredArray2(array):
    #initialize empty output array
    sortedSquares = [0 for _ in array]
    l_idx = 0  #points to the left most value in input array
    r_idx = len(array) - 1 #points to the right most value in input array
    curr_idx = len(array) - 1 # tracks index we are at currently
    while (l_idx <= r_idx):
        l_val = array[l_idx]
        r_val = array[r_idx]
        if abs(l_val)>= abs(r_val):
            sortedSquares[curr_idx] = array[l_idx] ** 2
            l_idx += 1
        elif abs(r_val) > abs(l_val):
            sortedSquares[curr_idx] = array[r_idx] ** 2
            r_idx -= 1
        curr_idx -= 1
    return sortedSquares