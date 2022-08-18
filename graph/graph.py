from collections import deque

class Queue:
    def __init__(self):
        self.deque = deque()

    def enqueue(self, value):
        self.deque.append(value)

    def dequeue(self):
        return self.deque.popleft()

    def __len__(self):
        return len(self.deque)


class Vertex:
    def __init__(self, value):
        """
        Node/vertex constructor
        """
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex


class Graph:
    def __init__(self):
        self.__adjacency_list = {}

    def add_node(self, value):
        """ Add the node to adj_list as key and value it will be an empty list"""
        vertex = Vertex(value)
        self.__adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adjacency_list or end_vertex not in self.__adjacency_list:
            raise KeyError("Start or End Vertex not found")

        if len(self.__adjacency_list) == 1: # For the case of having a graph with one vertex and one edge
            edge = Edge(end_vertex, weight)
            self.__adjacency_list[start_vertex].append(edge)
        else:
            edge1 = Edge(end_vertex, weight)
            edge2 = Edge(start_vertex, weight)
            self.__adjacency_list[start_vertex].append(edge1)
            self.__adjacency_list[end_vertex].append(edge2)

    def get_nodes(self):
        return self.__adjacency_list.keys()

    def size(self):
        return len(self.__adjacency_list)

    def get_neighbors(self, vertex):
        return self.__adjacency_list.get(vertex, [])

    def breadth_first(self, start_vertex):
        result = []
        visited = set()
        q = Queue()

        q.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(q):
            current_vertex = q.dequeue()
            result.append(current_vertex.value)

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.add(neighbor)
        return result


if __name__ == "__main__":
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    e = g.add_node('E')
    c = g.add_node('C')
    d = g.add_node('D')
    g.add_edge(a, b)
    g.add_edge(a, e)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(e, d)
    g.add_edge(e, c)

    print(g.breadth_first(a))
