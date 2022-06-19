#Implement Binary Search iterativley and Recursivley

"""
Binary Search Algorithm:
    - Ensure that the array is sorted in non-decreasing order
    Repeat the following:
    - Check the middle of array
    - If target is greater than middle value, search the right half of the array
    - If target is smaller than middle value, search the left half of array

    - Do this until you find value, if you check all values in array and can't find given value
    target is not in array

"""
#Note: When implementing we set start = mid + 1 and end = mid - 1, to avoid checking
#value at middle multiple times

def binarySearchIterative(array, target):
    """
    Time: O(logn), Space:O(1)
    """
    startIdx = 0
    endIdx = len(array) - 1
    while (startIdx <= endIdx):
        midIdx = (startIdx + endIdx) // 2
        if target < array[midIdx]:
            #search left half of subarray
            endIdx = midIdx - 1
        elif target > array[midIdx]:
            #search right half of subarray
            startIdx = midIdx + 1
        elif array[midIdx] == target:
            #value found at midIdx
            return midIdx
    return -1

def binarySearchRecursive(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    """
    Time: O(log n), Space: O(log n)
    """
    if left > right:
        return -1
    mid = (left + right) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        #search left subtree
        return binarySearchHelper(array, target, left, mid - 1)
    elif target > array[mid]:
        #search right subtree
        return binarySearchHelper(array, target, mid + 1, right)
