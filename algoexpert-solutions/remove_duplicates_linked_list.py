#AlgoExpert Easy Problem: Remove Duplicates Linked List

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


#1 -> 1 -> 3 -> 4 -> 4 -> 5
#check if self.next.value == self.value
#if it is then make self.next = self.next.next
#then continue for loop but don't change currNode
#if no more duplicates change curr node
        
#Time: O(n), traverse entire linked list
#Space: O(1)
def removeDuplicatesFromLinkedList1(linkedList):
    currNode = linkedList
    while True:
        if currNode.next is None:
            #end of linked list
            break
        if currNode.value == currNode.next.value:
            currNode.next = currNode.next.next
            continue
        currNode = currNode.next
        
    return linkedList

#AlgoExpert Solution
def removeDuplicatesFromLinkedList2(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        while nextNode is not None and nextNode.value == currentNode.value:
            nextNode = nextNode.next

        currentNode.next = nextNode
        currentNode = nextNode
    
    return linkedList