#Cracking the Coding Interview pg 94 2.1

"""
Prompt: Write code to remove duplicates from an unsorted linked list.
"""
from collections import defaultdict
class LinkedList:
    def __init__(self, data):
        self.value = data
        self.next = None

def remove_dups1(llist):
    """
        Time Complexity: O(n), traverse through entire linked list once
        Space Complexity: O(n), hashtable
    """
    numsFound = defaultdict(bool)
    currNode = llist

    #handle the head node
    if currNode is None:
        return currNode
    else:
        numsFound[currNode.value] = True

    while(currNode.next is not None):
        if numsFound[currNode.next.value]:
            #duplicate found, remove it
            currNode.next = currNode.next.next
        else:
            numsFound[currNode.next.data] = True
        currNode = currNode.next
    return llist

#Same solution as above, but we use previous pointer
def remove_dups2(llist):
    """
    Time Complexity: O(n), traverse through entire linked list once
    Space Complexity: O(n), hashtable
    """
    numsFound = defaultdict(bool)
    prev = None
    currNode = llist
    while (currNode is not None):
        if numsFound[llist.value]:
            #remove duplicate
            prev.next = currNode.next
        else:
            numsFound[currNode.next.value] = True
        prev = currNode
        currNode = currNode.next
    return llist

def remove_dups3(llist):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    currNode = llist
    prevNode = None
    while (currNode != None):
        searchNode = currNode.next
        while (searchNode != None):
            if searchNode.value == currNode.value:
                #remove duplicate
                prev.next = currNode.next
            searchNode = searchNode.next
        prev = currNode
        currNode = currNode.next
    return llist
