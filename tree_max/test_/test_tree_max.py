from tree_max import TNode, BinaryTree
import pytest


def test_max():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(9)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = tree.max_value()
    expected = 9
    assert actual == expected

def test_max_empty():
    tree = BinaryTree()
    actual = tree.max_value()
    expected = None
    assert actual == expected

def test_max_one_node():
    node1 = TNode(1)
    tree = BinaryTree()
    tree.root = node1
    actual = tree.max_value()
    expected = 1
    assert actual == expected

