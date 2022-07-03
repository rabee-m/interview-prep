#Cracking The Coding Interview 4.5 pg 110

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def validate_bst(root):
    return validate_bst_helper(root, float("-inf"), float("inf"))

def validate_bst_helper(node, left, right):
    if node is None:
        #base case
        return True
    
    if not (node.value < right and node.value > left):
        #check that current node is valid by making sure it is greater than right, andd less than left
        return False
    left_tree_valid = validate_bst_helper(node.left, left, node.value) #min value is still the same, but values can no longer be grater than node.value
    right_tree_valid = validate_bst_helper(node.right, node.value, right)
    
    if left_tree_valid and right_tree_valid:
        return True
    else: return False
    