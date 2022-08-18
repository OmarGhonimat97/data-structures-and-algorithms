import pytest
from graph.graph import *


def test_exists():
    assert Graph


def test_add_node():
    graph = Graph()
    actual = graph.add_node("test").value
    expected = "test"
    assert actual == expected


def test_add_edge():
    g = Graph()
    test1 = g.add_node("test1")
    test2 = g.add_node("test2")
    g.add_edge(test1, test2, 5)
    neighbors = g.get_neighbors(test1)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == "test2"
    assert neighbors[0].weight == 5


def test_get_nodes():
    graph = Graph()
    test1 = graph.add_node("test1")
    test2 = graph.add_node("test2")
    test3 = Vertex("test3")
    expected = 2
    actual = len(graph.get_nodes())
    assert actual == expected


def test_get_neighbors():
    graph = Graph()
    test1 = graph.add_node("test1")
    test2 = graph.add_node("test2")
    graph.add_edge(test2, test1, 8)
    neighbors = graph.get_neighbors(test2)
    assert len(neighbors) == 1
    neighbor_edge = neighbors[0]
    assert neighbor_edge.vertex.value == "test1"
    assert neighbor_edge.weight == 8


def test_size():
    graph = Graph()
    graph.add_node("test")
    actual = graph.size()
    expected = 1
    assert actual == expected


def test_graph_one_node_edge():
    g = Graph()
    test = g.add_node("test")
    g.add_edge(test, test, 10)
    neighbors = g.get_neighbors(test)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == "test"
    assert neighbors[0].weight == 10


def test_size_empty():
    graph = Graph()
    actual = graph.size()
    expected = 0
    assert actual == expected


