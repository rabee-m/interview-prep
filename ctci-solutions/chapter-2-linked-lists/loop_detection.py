#Cracking The Coding Interview pg 95 2.8
"""
Prompt: Given a circular linked list, implement an algorithm that returns the node
at the beginning of the loop

Cirucular Linked List: A (corupt) linked list in which a node's next pointer points to an
earlier node, so as to make a loop in the linked list
"""
from collections import defaultdict
class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def loopDetection(llist):
    #Loop through linked list adding values into a hashtable w/ booleans if they appeared
    nodeAppeared = defaultdict(bool)
    while (llist):
        if nodeAppeard[llist]:
            return llist
        else:
            nodeAppeard[llist] = True

#TODO: Finish this question