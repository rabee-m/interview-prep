#AlgoExpert Easy Problem: Implement Bubble Sort

"""
Bubble Sort Algorithm:
Iterate through array multiple times until it is fully sorted
During each iteration check if adjacent values are correctly positioned, if not perform a swap
Continue doing this until algorithm runs through array without performing any swaps, we then know the array is sorted
"""
def bubbleSort(array):
    """
    Time: O(n^2), Space: O(1)
    """
    isSorted = False
    while(not isSorted):
        isSorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
    return array

def swap(i, j, array):
    """
    Time: O(1), Space: O(1)
    """
    tmp = array[i]
    array[i] = array[i + 1]
    array[i + 1] = tmp