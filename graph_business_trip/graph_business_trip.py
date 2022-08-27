from graph.graph import *


def  business_trip(graph, cities):
    """ Returns True, cost if trip is possible, otherwise False, 0 """

    def direct(origin, destination):
        for v in graph.get_nodes():
            if v.value == origin:
                edges = graph.get_neighbors(v)
        for e in edges:
            if e.vertex.value == destination:
                return e.weight
        return False

    cost = 0
    for i in range(len(cities) - 1):
        origin = cities[i]
        destination = cities[i + 1]
        pair = direct(origin, destination)
        if not pair:
            return False, 0
        cost += pair
    return True, cost


if __name__ == '__main__':

    my_graph = Graph()

    a = my_graph.add_node("a")
    b = my_graph.add_node("b")
    c = my_graph.add_node("c")
    d = my_graph.add_node("d")
    e = my_graph.add_node("e")
    f = my_graph.add_node("f")

    my_graph.add_edge(b, a, 1)
    my_graph.add_edge(b, d)
    my_graph.add_edge(b, e)
    my_graph.add_edge(b, c, 3)

    my_graph.add_edge(c, f, 5)

    print(business_trip(my_graph , ["a", "b", "c", "f"]))
