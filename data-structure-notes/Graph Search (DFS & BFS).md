# Graph Search Algorithms
There are two main graph algorithms
- DFS (Depth-First Search) : Start at root (or arbitrarily selected node) and explore each branch completely before moving on to next branch
- BFS (Breadth-First Search) : Start at root (or arbitrarily selected node) and explore each neighbor before going on to any of their children
- DFS preferred if we want to visit every node in graph
- BFS preferred if we want to find shortest path between two nodes

## Depth-First Search (DFS) Implementation
<b>Overview:</b>
- Visit a node a and then iterate through each of a's neighbors
- When visiting a node b (neighbor of a), visit all of b's neighbors before going on to a's other neighbors

<b>Note:</b> Can implement pre-order, post-order, in-order traversal

<b>Pseduocode:</b>
```
void search(Node root) {
    if (root == null) return;
    visit(root);
    root.visited = true;
    for each (Node n in root.adjacent) {
        if (n.visited == false) {
            search(n)
        }
    }
}
```

## Breadth-First Search (BFS) Implementation
<p><b>Overview:</b></p>

- node a visits each of a's neighbors before visiting any of their neighbors (searching level by level from a)
- Iterativley implemented using a queue


<b>Note:</b> False assumption that BFS is recursive, it is iterative

<b>Pseduocode:</b>
```
void search(Node root) {
    Queue = queue = new Queue();
    root.marked = true;
    queue.enqueue(root); //add to end of queue

    while(!queue.isEmpty()) {
        Node r = queue.dequeue(); // Remove from front of the queue
        visit(r);
        foreach (Node n in r.adjacent) {
            if (n.marked == false) {
                n.marked = true;
                queue.enqueue(n);
            }
        }
    }
}
```

