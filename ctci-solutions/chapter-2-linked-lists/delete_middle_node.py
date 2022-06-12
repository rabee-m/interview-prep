#Creacking the Coding Interview pg 94 2.3
"""
Prompt: Implement an algorithm to delete a node in the middle (i.e) any node but first and last, not exactly middle)
of a singly linked list, given only access to that node.
"""
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

def delete_middle_node(node):
    """
        Time Complexity: O(1)
        Space: Complexity: O(1)
        Strategy: Copy over next node value to currNode, and then delete the next node
    """
    node.value = node.next.value
    node.next = node.next.next 