import pytest
from graph_depth_first.graph_depth_first import *


def test_multiple(graph):
    root = graph.get_nodes()[0]
    print(root)
    actual = graph.depth_first(root)
    expected = ["a", "b", "c", "g", "d", "e", "h", "f"]
    assert actual == expected


def test_empty():
    graph = Graph()
    node = Vertex("test")
    actual = graph.depth_first(node)
    expected = []
    assert actual == expected


def test_one_vertex():
    graph = Graph()
    test = graph.add_node("test")
    actual = graph.depth_first(test)
    expected = ["test"]
    assert actual == expected


def test_two_vertices():
    graph = Graph()
    test1 = graph.add_node("test1")
    test2 = graph.add_node("test2")
    graph.add_edge(test1, test2)
    actual = graph.depth_first(test1)
    expected = ["test1", "test2"]
    assert actual == expected

@pytest.fixture
def graph():

    letters = Graph()

    a = letters.add_node("a")
    b = letters.add_node("b")
    c = letters.add_node("c")
    d = letters.add_node("d")
    e = letters.add_node("e")
    f = letters.add_node("f")
    g = letters.add_node("g")
    h = letters.add_node("h")

    letters.add_edge(a, b)
    letters.add_edge(b, c)
    letters.add_edge(c, g)
    letters.add_edge(a, d)

    letters.add_edge(d, e)
    letters.add_edge(d, h)
    letters.add_edge(d, f)

    letters.add_edge(h, f)

    return letters

