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
        

def routeBetweenTwoNodes(n1, n2):
    #start at n1 and perform a DFS
    stack = []
    stack.append(n1)
    
    while (len(stack) != 0):
        currNode = stack.pop()
        currNode.visited = True
        if (n2 == currNode): return True
        for adjNode in currNode.adjNodes:
            stack.append(adjNode)
    
    return False
            