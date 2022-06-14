#Cracking the Coding Interview pg 95 2.6
"""
Prompt: Implement a function to check if a linked list is a palindrome
"""
class LinkedList:
    def __init__(self, data):
        self.value = data
        self.next = None

#A -> B -> C -> D -> None
# D -> C -> B -> A -> None

prev = None
nextNode = currNode.next
currNode.next = prev
prev = currNode

#A->None
#B-> A- > None
"""
Strategy: Two Pointer Approach (Fast & Slow Pointer)
- Intialize two pointers: a fast pointer and slow pointer
- The fast pointer will move two positions for every position that the slow pointer moves
- Once the fast pointer reaches end of linked list, the slow pointer will be at the middle of the
linked list
- Reverse the 2nd half of the linked list, then compare values
"""

def palindromeCheck(llist):
    fastPtr = llist
    slowPtr = llist
    while fastPtr and fastPtr.next:
        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next
    
    #slowPtr is at half of linked list, reverse 2nd half of linked lsit
    prevNode = None
    currNode = slowPtr
    while(currNode):
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    
    l, r = llist, prevNode #prevNode will be last node in llist, as slowPtr will be null and prevNode will be before it
    while l is not None and r is not None:
        if l.value != r.value: return False
        l, r = l.next, r.next
    return True
    
