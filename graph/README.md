# Graphs
<!-- Short summary or background information -->

## Challenge
<!-- Description of the challenge -->
Implement a graph represented as an adjacency list with the following methods:

- add node
- add edges
- get nodes
- get neighbors
- size


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The graph is implemented as an adjacency list. The adjacency list is a dictionary (hash table). The keys are the vertices and the values are the edges. Each edge has a vertex to which it points and a weight (default 0).

The operations (add node, get nodes, size, add edge and get neighbors) have an O(1) time complexity. This is because we use a dictionary for the adjacency list.

## API
<!-- Description of each method publicly available in your Graph -->


> add_node: 

adds a node to the graph

- Arguments: value
- Returns: the added node

> add_edge: 

adds a new edge between two nodes in the graph, if specified, assigns a weight to the edge; default 0. Raises a Key error if either node is not in the graph.

- Arguments: 2 nodes to be connected by the edge, weight
- Returns: nothing

> get_nodes:

- Arguments: none
- Returns: all of the nodes in the graph as a collection

> get_neighbors:

- Arguments: node
- Returns: a collection of edges connected to the given node, including the weight of the connection

> size:

- Arguments: none
- Returns: the total number of nodes in the graph



