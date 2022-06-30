#Cracking The Coding Interview 4.1 pg 109

"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes
"""
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

class Node:
    def __init__(self, value, adjNodes):
        self.value = value
        self.adjNodes = adjNodes
        self.visited = False
        

def routeBetweenTwoNodesDFS(n1, n2):
    #start at n1 and perform a DFS
    stack = []
    stack.append(n1)
    
    while (len(stack) != 0):
        currNode = stack.pop()
        currNode.visited = True
        if (n2 == currNode): return True
        for adjNode in currNode.adjNodes:
            if (not currNode.visited):
                stack.append(adjNode)
    
    return False

def routeBetweenTwoNodesBFS(n1, n2):
    queue = []
    queue.append(n1)
    
    while (len(queue) != 0):
        currNode = queue.pop(0)
        if (currNode == n2): return True
        for adjNode in currNode.adjNodes:
            if (currNode.marked == False):
                currNode.marked = True
                queue.append(currNode)
    return False
        
            