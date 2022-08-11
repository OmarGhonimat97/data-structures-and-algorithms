import pytest
from tree_intersection.tree_intersection import tree_intersection
from trees.trees import BinaryTree, TNode
from stack_and_queue.stack_and_queue import Queue


def test_small():
    tree_a = BinaryTree()
    values = [1, 5]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = [4, 5]
    add_values_to_empty_tree(tree_b, values)
    actual = tree_intersection(tree_a, tree_b)
    expected = [5]
    assert sorted(actual) == sorted(expected)


def test_no_common():
    tree_a = BinaryTree()
    values = [1, 5]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = [4, 2]
    add_values_to_empty_tree(tree_b, values)
    actual = tree_intersection(tree_a, tree_b)
    expected = []
    assert sorted(actual) == sorted(expected)


def test_one_empty():
    tree_a = BinaryTree()
    values = [1, 5]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = []
    add_values_to_empty_tree(tree_b, values)
    actual = tree_intersection(tree_a, tree_b)
    expected = []
    assert sorted(actual) == sorted(expected)


def test_almost_same():
    tree_a = BinaryTree()
    values = [1, 5, 7, 9]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = [1, 5, 7, 9, 11]
    add_values_to_empty_tree(tree_b, values)
    actual = tree_intersection(tree_a, tree_b)
    expected = [1, 5, 7, 9]
    assert sorted(actual) == sorted(expected)


def test_tree_intersection():
    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)
    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)
    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]
    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    if values:
        tree.root = TNode(values.pop())
        q = Queue()
        q.enqueue(tree.root)
        while values:
            node = q.dequeue()
            node.left = TNode(values.pop())
            node.right = TNode(values.pop()) if values else None
            q.enqueue(node.left)
            q.enqueue(node.right)