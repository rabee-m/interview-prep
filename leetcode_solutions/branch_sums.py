#AlgoExpert Easy Problem: Branch Sums

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Time: O(n), traversing the every node in Binary Tree
#Space: average O(log n) worst O(n), recursive call stack is being eliminated once you get sum of branch
def branchSums(root):
    sums = []
    branchSumsHelper(root, 0, sums)
    return sums

def branchSumsHelper(node, runningSum, sums):
    if node is None:
        return
    newRunningSum = node.value + runningSum
    #check if we are at a leaf node, if so append sum
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    
    branchSumsHelper(node.left, newRunningSum, sums)
    branchSumsHelper(node.right, newRunningSum, sums)