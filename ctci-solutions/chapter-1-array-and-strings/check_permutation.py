#Cracking the Coding Interview Q 1.2, pg 90
from collections import defaultdict
"""
Given two strings, write a method to decide if one is a permutation of the other
"""

#Solution 1: Use a Hash Map
#Time: O(n1 + n2) ,where n1 and n2 are lengths of s1 and s2
#Space: O(max(n1, n2)), due to hashmap
def checkPermutation(s1, s2):
    hashMap = defaultdict(int)
    for c in s1:
        hashMap[c] += 1
    
    for c in s2:
        hashMap[c] -= 1
    
    for val in hashMap.values():
        if val != 0:
            return False
    return True

#Solution 2: Sort Arrays
#Time: O(n*logn), due to sorting
#Space: O(1)

def checkPermutation2(s1, s2):
    s1.sort()
    s2.sort()
    return s1 == s2

print(checkPermutation("taco", "ocat"))
print(checkPermutation("taco", "tacooo"))