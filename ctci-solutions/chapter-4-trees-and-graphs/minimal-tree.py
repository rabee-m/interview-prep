#Cracking The Coding Interview 4.2 pg 109

"""
Prompt: Given a sorted(increasing order) array with unique integer elements,
write an algoritm to create a binary search tree with minimal height
"""

"""
Take middle element make it the root
build left subtree from left half
build right subtree from right half
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def minimal_tree(arr):
    """
    Time: O(n), traverse all elements
    Space: O(log n), half elements on call stack before returned
    """
    return minimal_tree_helper(arr, 0, len(arr) - 1)

def minimal_tree_helper(arr, start, end):
    if (end < start):
        return None
    
    midIdx = (start + end) / 2
    currNode = Node(arr[midIdx])
    
    currNode.left(minimal_tree_helper(start, midIdx -1))
    currNode.right(minimal_tree_helper(midIdx + 1, end))
    
    return currNode