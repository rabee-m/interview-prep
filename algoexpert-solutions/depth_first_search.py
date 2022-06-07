#AlgoExpert Easy Problem: Depth First Search

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

#Time: O(v + e), every node(vertex) is traversed that is how we get O(v),
#at every vertex, we iterrate through children(edges) calling DFS

#Space: O(v), array holds all vertex names, and DFS also takes additional O(v)
#space because the call-stack is not returned until we traverse all childs of root
# if graph looks like A-B-C-D-E-F-..., we would have v frames on the call-stack
# worst case
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array