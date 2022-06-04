---
tags: [Data Structures]
title: Binary Search Tree(BST)
created: '2022-06-04T03:45:48.781Z'
modified: '2022-06-04T04:07:59.002Z'
---

# Binary Search Tree(BST)

## Overview
<p> A Binary Search Tree aims to solve the following problems:
<ul>
  <li>a) Search(x) </li>
  <li>b) Insert(x) </li>
  <li>c) Remove(x) </li>
</ul>
<p> <b>Note:</b> x is an element in the data </p>
<p> Binary search tree aims to allow for all operations mentioned earlier (similar to array, or linked list), whilst minimizing time complexity for each to O(log n) on average, as long as tree is relatively balanced.

## Implementation
<p> Binary search tree maintains the following structure within data:
<ul>
  <li>For each node, value of all nodes in left subtree is less or equal</li>
  <li>For each node, value of all nodes in right subtree is greater</li>
</ul>
<p>The following depicts valid BST vs not valid BST: </p>
![bst_valid_vs_not_valid](imgs/valid_bst_vs_not_valid.png).



### Searching for value in BST
<p> Searching BST for a value follows algorithm similar to binary search. We essentially compare value to root, if it's less than we search left subtree, if it's greater than, we search right subtree until we find equality or traverse entire tree. </p>
<p> <b>Time Complexity:</b> O(log n) for balanced BST, O(n) worse case

### Unbalanced BST
<p> Unbalanced BST is when sorted values are inserted into BST, and we end up with one long right subtree, or left subtree which is similar to a linked list </p>



