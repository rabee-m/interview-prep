#Cracking the Coding Interview pg 94 2.4
"""
Prompt: Write code to partition a linked list around a value x, such that all nodes less than x,
come before all nodes greater than or equal to x. If value x appears in list it can appear anywhere
within the right partition.
"""
class LinkedList:
    def __init__(self, data):
        self.value = data
        self.next = None


def insert_node(llist, node):
    if llist is None:
        llist = node
    else:
        llist.next = node

def partition(llist, p_val):
    left_partition = None
    left_partition_len = 0
    right_partition = None
    right_partition_len = 0

    currNode = llist
    while(currNode):
        if currNode.value < p_val:
            insert_node(left_partition, currNode)
            left_partition_len += 1
        else:
            insert_node(right_partition, currNode)
        currNode = currNode.next
        right_partition_len += 1
    
    #Change the last element left_partition is pointing to, to be the right partition, and
    #change the last element right_partition is point to, to be none
    left_partition_node = left_partition
    idx = 0
    while (idx != left_partition_len):
        left_partition_node = left_partition.next
    left_partition_node.next = right_partition

    right_partition_node = right_partition
    idx = 0
    while (idx != right_partition_len):
        right_partition_node = right_partition.next
    right_partition.next = None
