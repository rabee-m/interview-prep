# Heaps

## Overview
<ul>
    <li> Heaps can come in two different forms: a min heap or max heap </li> 
</ul>
<p> <b>Note: </b>Focus on min heap, max heap will be the same except with max node at top </p>
<p> A min heap is a tree where the elements are all smaller than their children i.e) when we traverse down the tree values decrease. By this convention, we know tbe root node will be the smallest value. </p>

###  Insert
<p> When we insert element into heap, we always start by inserting into last possible location going from top to bottom, left to right. Then we "fix" the tree by swapping the new element with it's parent until we find appropriate space. </p>

### Extract Min (Removing Min)
<p> <b> Note:</b> min element is rootNode in min heap</p>
<p> To remove the smallest value in a min heap, we remove the root by swapping it with the last element in the heap (bottom-most, right-most element). Then we bubble down swapping it with one of its children until the minHeap proprty is restored.</p>

## Implementation
<p> Instead of implementing a heap w/ HeapNodes, we can implement it as an array since, there are no gaps in the heap as we always insert into next possible element. </p>
<ul>
    <li> Contains items in a dynamically sized array </li>
</ul>

<a href= "https://www.youtube.com/watch?v=t0Cq6tVNRBA&t=361s"> useful video </a>