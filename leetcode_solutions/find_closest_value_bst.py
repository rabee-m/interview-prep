#AlgoExpert Easy Problem: Find Closest Value in BST
"""
Prompt: Given a BST and target value, find the closest value in the BST
to given target value
"""
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Iterative solution
# Average: time is O(log(n)), space is O(1)
#Worse: O(n) time, O(1) space

def findClosestValueInBstHelper1(tree, target, closest_val):
    currentNode = tree
    while currentNode is not None:
        #check if there is a new closet value
        if abs(currentNode.value - target) < abs(closest_val - target):
            closest_val = currentNode.value
        if currentNode.value == target:
            #found value we are searching for
            return currentNode.value
        elif currentNode.value < target:
            #search right subtree
            currentNode = currentNode.right
        elif currentNode.value > target:
            #search left subtree
            currentNode = currentNode.left
    return closest_val
                    
def findClosestValueInBst1(tree, target):
    return findClosestValueInBstHelper1(tree, target, tree.value)

#Recursive solution
# Average: time is O(log(n)), space is O(log(n))
#Worse: O(n) time, O(n) space
def findClosestValueInBstHelper2(tree, target, closest):
    if tree is None:
        #Base case
        return closest
    if abs(target - tree.value) < abs(target - closest):
        closest = tree.value
    if tree.value < target:
        #search right subtree
        return findClosestValueInBstHelper2(tree.right, target, closest)
    elif tree.value > target:
        #search left subtree
        return findClosestValueInBstHelper2(tree.left, target, closest)
    elif tree.value == target:
        return tree.value
        
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper2(tree, target, tree.value)