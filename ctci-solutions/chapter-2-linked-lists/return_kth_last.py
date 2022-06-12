#Cracking the Coding Interview pg 94 2.2
"""
Prompt: Implement an algorithm to find the kth to last element of a singly linked list
"""

class LinkedList:
    def __init__(self, data):
        self.value = data
        self.next = None

"""
    Strategy: Two Pointer Approach(Iterative):
    -Create two pointers, one fast_ptr, that starts at position k, and one slow_ptr that starts at beginning of list
    - Traverse through linkedlist, incrementing both pts by one, once the fast_ptr reaches null node, then the slow_ptr
    will be exactly kth elements from fast_ptr which in this case is kth elements from the last element.
"""

def remove_kth_last_element_iterative(llist, k):
    """
        Time Complexity: O(n), traverse through linked list once
        Space Complexity: O(1)
    """
    slow_ptr = llist
    fast_ptr = llist
    #move fast_ptr to kth pos in llist
    idx = 0
    while (fast_ptr):
        idx += 1
        fast_ptr = fast_ptr.next

    #Traverse to the end of the linked list
    while(fast_ptr):
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    
    return slow_ptr.value

#TODO: Add recursive solution