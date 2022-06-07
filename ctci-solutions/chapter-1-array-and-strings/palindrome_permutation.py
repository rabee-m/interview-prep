#Cracking the Coding Interview pg 91 1.4
from collections import defaultdict
"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. Palindrome does not need to be limited to
just dictionary words.
"""
def palindromePermutation(s):
    
    """
    String can be even or odd length
    e.g.) taaat and taat
    if even:
        all characters must appear even number of times
    if odd:
        all charcters must appear even number of times, except for one character which can appear odd number of time
    """
    countChars = defaultdict(int)
    for c in s:
        countChars[c] += 1
    
    if len(s) % 2 == 0:
        #even string
        for val in countChars.values():
            if val % 2 != 0:
                return False
    else:
        #odd string
        foundOdd = False
        for val in countChars.values():
            if val % 2 ==  1 and foundOdd:
                return False
            elif val %2  == 1:
                foundOdd = True
    return True

#We can simplify the algorithm above by recogonizing, that we don't have to check whether strings are even or odd
#as if a string is even, it cannot have only one odd character appearing, and must have multiple odd characters, so we can
#check if more than one odd character appears. and similarly with odd length strings we are already checking the condition
#that only one character appears odd amount of times
def palindromePermutationSimplified(s):
    countChars = defaultdict(int)
    
    for c in s:
        countChars[c] += 1

    bool oddFound = False
    for val in countChars.values():
        if val % 2 == 1 and oddFound:
            return False
        elif val % 2 == 1:
            oddFound = True
    return True