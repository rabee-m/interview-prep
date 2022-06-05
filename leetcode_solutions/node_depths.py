##AlgoExpert Easy Problem: Node Depths
# Time: O(n), traverse every node in tree
#Space: O(log n)/O(h) as call stack is returned after branch is traversed
def nodeDepths(root):
    return nodeDepthsHelper(root, 0)

def nodeDepthsHelper(node, runningDepth):
    if node is None:
        return 0
    else:
        #increment depth by 1 when calling leftDepths and rightDepths func
        #as they are 1 layer deeper
        leftDepths = nodeDepthsHelper(node.left, runningDepth + 1)
        rightDepths = nodeDepthsHelper(node.right, runningDepth + 1)
        return runningDepth + leftDepths + rightDepths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None