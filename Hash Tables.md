---
tags: [Data Structures]
title: Hash Tables
created: '2022-05-31T19:43:28.682Z'
modified: '2022-05-31T20:19:23.448Z'
---

# Hash Tables

## Overview
<p> A Hash Table is a data structure that combines the random access ability of an array with the dynamism of a linked list. </p>
<ul>
  <li> Lookup tends toward O(1) similar to an array. (Don't need to traverse linked list for lookup)</li>
  <li> Insertion tends toward O(1) similar to linked list. (Don't need to dynamically resize array) </li>
</ul>
<p>Data itself gives us a clue about where we will find the data, should we need to look it up. </p>
<p><b>Downside:</b> Bad at ordering and sorting data </b></p>
<p> Only use hash-table if you don't care about sorting or ordering of data elements</p>

## Implementation
<p>Combination of two things:</p>
<ol>
  <li><b>Hash Function</b>: which returns an nonnegative integer value called a hash code.</li>
  <li><b>Linked List/Array</b>: capable of storing data of the type we wish to place into data structure </li>
</ol>
<p><b>Idea:</b> Run data through hash function, then store data in the index of arrray repersented by the returned hash code</p>

### Collision and Chaining
<p><b>Collision</b>: occurs when two pieces of data generate the same hashcode when run through the hash function.</p>
<p><b>Chaining</b>: Each index corresponds with a linked list, and if there is a collision(2 entries giving same hashcode) we insert into linked list at that index (Insertion: O(1)) </p>
<p><b>Note:</b> Lookup can still be approximated towards O(1) as when we lookup a value we are not traversing one huge list but instead across n smaller lists.</p>

<p>Helpful Video Link: https://www.youtube.com/watch?v=nvzVHwrrub0&ab_channel=CS50 </p>

