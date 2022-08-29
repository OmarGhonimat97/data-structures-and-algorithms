# Depth First Traversal
<!-- Short summary or background information -->


## Challenge
<!-- Description of the challenge -->
Write the following method for the Graph class:

- Name: Depth first
- Arguments: Node (Starting point of search)
- Return: A collection of nodes in their pre-order depth-first traversal order

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The traversal, by looking at all edges, visits each vertex once and adds it to the visited list. Also, worse-case, the call stack may approach the number of vertices.

- Time: O(v+e) 
- Space: O(v+e)


## Solution
<!-- Embedded whiteboard image -->

## Requirements
Tests passes:

- Empty graph / root not in graph
- Single vertex
- Multiple vertices and multiple edges
- Two vertices
