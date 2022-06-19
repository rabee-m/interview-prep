#AlgoExpert Easy Question: Find Three Largest Numbers
def findThreeLargestNumbers(array):
    maxNums = [None, None, None]
    for num in array:
        if maxNums[2] is None or num > maxNums[2]:
            shiftAndUpdate(maxNums, num, 2)
        elif maxNums[1] is None or num > maxNums[1]:
            shiftAndUpdate(maxNums, num, 1)
        elif maxNums[0] is None or num > maxNums[0]:
            shiftAndUpdate(maxNums, num, 0)
    return maxNums

def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]