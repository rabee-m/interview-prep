#Cracking the Coding Interview pg 95 2.7
"""
Given two singly linked lists, determine if the two liss intersect. Return
the intersecting node. Note that intersection is defined based on reference, not value. 
"""

class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next
"""
Strategy:   
"""


def intersection_llist(llist1, llist2):
    #Get length of both linked lists and last nodes
    lastNode1 = llist1
    lenList1 = 1
    if lastNode1 is not None:
        while(lastNode1.next):
            lastNode1 = lastNode1.next 
            lenList1 += 1
    lastNode2 = llist2
    lenList2 = 1
    if lastNode2 is not None:
        while(lastNode2.next):
            lastNode2 = lastNode2.next
            lenList2 += 1
    if lastNode1 != lastNode2: return False

    #calclulate the smaller list
    smallerListNode = llist1 if lenList1 < lenList2 else llist2
    biggerListNode = llist1 if lenList1 >= lenList2 else llist1
    offset = abs(lenList1 - lenList2)
    while (True):
        if offset != 0:
            biggerListNode = biggerListNode.next
            offset -= 1
            continue
        if smallerListNode == biggerListNode: return smallerListNode
    

