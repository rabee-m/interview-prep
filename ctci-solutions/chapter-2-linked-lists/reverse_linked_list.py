#General Question about Reversing a linked list iterativley and recursivley
class ListNode:
    def init(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseLinkedListIterative(head: ListNode):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    prevNode = None
    currNode = head
    while (currNode):
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    return prevNode

#TODO: Understand recursive implementation


