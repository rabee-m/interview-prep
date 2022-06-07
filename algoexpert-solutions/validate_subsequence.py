#AlgoeExpert Easy Problem: Validate Subsequence
#Solution: Loop through the array once, checking tracking index of sequence, and when we find element in sequence, we
#increment our idx by 1. If idx is equal to the length of our sequence, we have a valid subsequence
#Time:O(n), since we are traversing array once
#Space:O(1)
def isValidSubsequence(array, sequence):
    idx = 0
    for num in array:
        if idx == len(sequence):
            break
        if sequence[idx] == num:
            idx += 1

    return idx == len(sequence)