#Cracking the Coding Interview 4.4 pg 110
"""
Prompt: Implement a function to check if a binary tree is balanced.
For the purpose of this question, a balanced tree is defined to be a tree such that the height of the two subtrees of any node
never differ by more than one
"""

#Solution inspired from Neetcode: Balanced Binary Tree - Leetcode 110 - Python

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def isBalanced(root):
    return dfs(root)[0]

def dfs(root):
    if root is None: return [True, 0]
    
    left, right = dfs(root.left), dfs(root.right)
    isbalanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
    return [isbalanced, 1 + max(left[1], right[1])]

