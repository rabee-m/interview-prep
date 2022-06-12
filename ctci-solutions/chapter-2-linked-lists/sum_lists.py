#Cracking the Coding Interiew pg 95 2.5
"""
Prompt: You have two numbers repersented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
e.g.) 7 -> 1 -> 6 + 5 -> 9-> 2 is 617 + 295 and output is 2 -> 1 -> 9
"""

class LinkedList:
    def __init__(self, data):
        self.value = data
        self.next = None

def sum_lists_reverse(llist1, llist2):
    currNode1 = llist1
    currNode2 = llist2
    carryOver = 0
    sum_llist = None
    while (currNode1 is not None and currNode2 is not None):
        #null nodes have value 0
        valNode1 = currNode1.value if currNode1 is not None else 0
        valNode2 = currNode2.value if currNode2 is not None else 0

        valNewNode = (valNode1 + valNode2 + carryOver) % 10 
        carryOver = (valNode1 + valNode2) // 10
        NewNode = LinkedList(valNewNode)
        if sum_llist is None:
            sum_llist = NewNode
        else:
            sum_llist.next = NewNode
        
        #update nodes
        currNode1 = currNode1.next if currNode else None
        currNode2 = currNode2.next if currNode else None
    
    return sum_llist

#Add forward sum implementation