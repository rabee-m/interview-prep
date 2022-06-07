##AlgoExpert Easy Problem: Node Depths

#Recursive Approach
# Time: O(n), traverse every node in tree
#Space: O(log n)/O(h) as call stack is returned after branch is traversed
def nodeDepths1(root):
    return nodeDepthsHelper1(root, 0)

def nodeDepthsHelper1(node, runningDepth):
    if node is None:
        return 0
    else:
        #increment depth by 1 when calling leftDepths and rightDepths func
        #as they are 1 layer deeper
        leftDepths = nodeDepthsHelper1(node.left, runningDepth + 1)
        rightDepths = nodeDepthsHelper1(node.right, runningDepth + 1)
        return runningDepth + leftDepths + rightDepths

#Iterative approach
#Time: O(n), as we traverse every node to get depth
#Space: O(h), as we store branches in a stack
def nodeDepths2(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while (len(stack) > 0):
        nodeInfo = stack.pop()
        currNode = nodeInfo['node']
        currDepth = nodeInfo['depth']
        
        if currNode is None:
            #skip None nodes
            continue
        sumOfDepths += currDepth
        stack.append({"node": currNode.left, "depth": currDepth + 1})
        stack.append({"node": currNode.right, "depth": currDepth + 1})
        
    return sumOfDepths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None