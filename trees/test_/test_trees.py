from trees import TNode, BinaryTree, BinarySearchTree
import pytest


def test_empty_tree():
    tree = BinaryTree()
    assert tree.root == None


def test_single_root_tree():
    tree = BinaryTree()
    node1 = TNode(10)
    tree.root = node1
    assert tree.root.value == 10


def test_pre_order():

    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = tree.pre_order()
    expected = [1, 2, 3, 4]
    assert actual == expected


def test_in_order():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = tree.in_order()
    expected = [2, 1, 3, 4]
    assert actual == expected


def test_post_order():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = tree.post_order(tree.root)
    expected = [2, 4, 3, 1]
    assert actual == expected


def test_binary_search_tree_pre_order():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    bst = BinarySearchTree()
    bst.root = node1
    bst.add(7)
    actual = bst.pre_order()
    expected = [1, 2, 3, 4, 7]
    assert actual == expected


def test_binary_search_tree_post_order():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    bst = BinarySearchTree()
    bst.root = node1
    bst.add(8)
    actual = bst.post_order(bst.root)
    expected = [2, 8, 4, 3, 1]
    assert actual == expected


def test_binary_search_tree_in_order():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    bst = BinarySearchTree()
    bst.root = node1
    bst.add(7)
    actual = bst.in_order()
    expected = [2, 1, 3, 4, 7]
    assert actual == expected

