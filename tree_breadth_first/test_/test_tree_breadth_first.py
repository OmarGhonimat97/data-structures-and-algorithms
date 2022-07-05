import pytest
from tree_breadth_first import *

def test_breadth_first():

    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = breadth_first(tree)
    expected = [1, 2, 3, 4]
    assert actual == expected

def test_breadth_first_empty():

    tree = BinaryTree()
    actual = breadth_first(tree)
    expected = "Tree is empty"
    assert actual == expected
