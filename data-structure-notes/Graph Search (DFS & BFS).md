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
- Iterativley implemented using a <b>stack</b>

<b>Note:</b> Can implement pre-order, post-order, in-order traversal

<b>Pseduocode:</b>

Recursive:
```
void recursiveDFS(Node root) {
    if (root == null) return;
    visit(root);
    root.visited = true;
    for each (Node n in root.adjacent) {
        if (n.visited == false) {
            recursiveDFS(n)
        }
    }
}
```

Iterative:
```
void iterativeDFS(Node root) {
    Stack stack = new Stack();
    stack.append(root)

    while(!stack.isEmpty()) {
        Node r = stack.pop();
        visit(r);
        r.visited = true;
        foreach(Node n in r.adjacent) {
            if (!n.visited) {
                stack.append(n)
            }
        }
    }
}
```

## Breadth-First Search (BFS) Implementation
<p><b>Overview:</b></p>

- node a visits each of a's neighbors before visiting any of their neighbors (searching level by level from a)
- Iterativley implemented using a <b>queue</b>


<b>Note:</b> False assumption that BFS is recursive, it is iterative

<b>Pseduocode:</b>
```
void iterativeBFS(Node root) {
    Queue queue = new Queue();
    root.marked = true;
    queue.enqueue(root); //add to end of queue

    while(!queue.isEmpty()) {
        Node r = queue.dequeue(); // Remove from front of the queue
        visit(r);
        foreach (Node n in r.adjacent) {
            if (n.marked == false) {
                n.marked = true; // to keep track of what nodes are in queue
                queue.enqueue(n);
            }
        }
    }
}
```

Helpful youtube link: https://www.youtube.com/watch?v=pcKY4hjDrxk&ab_channel=AbdulBari
