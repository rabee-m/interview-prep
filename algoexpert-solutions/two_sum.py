#AlgoExpert Easy problem: Two Number Sum


#Solution 1: Run a double for-loop, looping through each value, then adding it to the remaining values 
#within the array, and checking if it is equal to the targetSum.
#Time: O(N^2) due to the double for-loops
#Space:O(1) not storing any additional values

def twoNumberSum1(array, targetSum):
    for i in range(len(array)):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

#Solution 2: Loop through the array once storing each value in a hash table, and checking if the 
# complement: TargetSum - num is in the complements hashmap. If it is return num and the complement
#Time: O(N), looping through the array once
#Space:O(N), storing values in a hash table

def twoNumberSum2(array, targetSum):
    complements = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in complements:
            return [num, lookup_val]
        complements[num] = True #add current num into the dictionary
    return []

#Solution 3: Sorting the array then intializing two pointers, pointing to the last and first index. Then based on
#whether the sum is greater or less than the target sum we adjust the pointers. If the pointers cross, targetSum cannot be found
#otherwise we will find the indicies of targetSum
#Time: O(N*logN), due to sorting the array
#Space: O(1), not storing any values
def twoNumberSum3(array, targetSum):
    array.sort() #Quicksort complexity is O(NlogN)
    i = 0
    j = len(array) - 1
    while(i < j):
        if array[i] + array[j] < targetSum:
            i += 1
        elif array[i] + array[j] > targetSum:
            j -= 1
        elif array[i] + array[j] == targetSum:
            return [array[i], array[j]]
    return []
