#Cracking The Coding Interview pg 91 1.5

"""
Prompt: There are three types of edits that can be performed on strings:
    - insert a character
    - remove a character
    - replace a character
Given two strings write a function to check if they are one edit (or zero edits away)
"""

"""
Case 1: Check for Replacement (occurs when lengths of s1 and s2 are same):
    - If a string has been replaced, then both strings will have identical characters differing by only one value.
    - To check for replacement we will essentially, loop through the arrays and make sure all values are the same
        allowing for a difference of one character

Case 2: Check for insertion (occurs when s1 is one character longer than s2):
    - Loop through s1 and s2, comparing each value. All values should be identical until we run into one different value. We ignore
    that value, then continue comparing, as all other values should still match.

Case 3: Check for removal (occurs when s1 is one less character shorter than s2):
    - Removal is essentially insertion but the other way around. We can instead check if s2 has a value inserted into it compared to s1
    - e.g.) Appl and Apple is a removal, but it can also be an insertion as Apple has letter e inserted into it compared to Appl
    - We can call same function for insertion but in reverse
"""

def checkReplace(s1, s2):
    differenceFound = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if differenceFound: return False
            differenceFound = True
    return True

def checkInsert(s1, s2):
    #Check that s1 is an insertion away from s2 
    index1 = 0
    index2 = 0
    differenceFound = False
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if differenceFound: return False
            differenceFound = True
            index1 += 1
        index1 += 1
        index2 += 1
    return True

def oneEditAway(s1, s2):
    if len(s1) == len(s2):
        #Case: Check for replacement
        return checkReplace(s1, s2)
    elif len(s1) + 1 == len(s2):
        #S1 has a character inserted into it, or S2 has a character removed
        return checkInsert(s1, s2)
    elif len(s2) + 1 == len(s1):
        #S2 has a character inserted into it// s1 has a character removed
        return checkInsert(s2, s1)
    else:
        return False

