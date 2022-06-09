#Cracking the Coding Interview, pg 91 1.6
from collections import defaultdict

"""
    Prompt: Implement a method to perform basic string compression using counts of repeated characters
    e.g.) aabcccccaaa becomes a2b1c5a3. If the "compressed" string would not become smaller than original
    string, your methoud should return the original string. You can assume string has only upper and lowercase
    letters (a-z)
"""

#Time: O(n), loop through string once
#Space: O(n), create new string based on size of input

def stringCompression(s):
    #set values for first index
    prevChar = s[0]
    runningCharCount = 1
    compressedString = "" 
    #loop through first and last index
    for i in range(1, len(s)):
        if s[i] == prevChar:
            runningCharCount += 1
        elif s[i] != prevChar:
            compressedString = compressedString + prevChar + str(runningCharCount)
            runningCharCount = 1
        prevChar = s[i]
    
    #add last element to compressedString
    compressedString = compressedString + prevChar + str(runningCharCount)
    if len(compressedString) > len(s):
        return s
    else:
        return compressedString


print(stringCompression("aabccccca"))
