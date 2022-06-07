#Cracking the Coding Interview Q 1.1, pg 90
from collections import defaultdict

"""
Prompt:
Implement an algorithm to determine if a string has all unique characters.
"""

#Solution 1: Hashtable
#Time: O(n)
#Space: O(n), due to hash map
def is_unique(s):
    charAppears = defaultdict(bool)
    for c in s:
        if charAppears[c]:
            return False
        charAppears[c] = True
    return True

#Solution 2: Sorting the array
#Time: O(n*logn), due to sorting
#Space: O(n)
def is_unique2(s):
    list_s = list(s)
    list_s.sort()
    for i in (range(len(s) - 1)):
        if list_s[i] == list_s[i+1]:
            return False
    return True

print(is_unique("tooy"))