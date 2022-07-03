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

    node1 = TNode(10)
    node2 = TNode(20)
    node3 = TNode(30)
    node4 = TNode(40)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = tree.pre_order()
    expected = [10, 20, 30, 40]
    assert actual == expected


def test_in_order():
    node1 = TNode(10)
    node2 = TNode(20)
    node3 = TNode(30)
    node4 = TNode(40)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = tree.in_order()
    expected = [20, 10, 30, 40]
    assert actual == expected


def test_post_order():
    node1 = TNode(10)
    node2 = TNode(20)
    node3 = TNode(30)
    node4 = TNode(40)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = tree.post_order(tree.root)
    expected = [20, 40, 30, 10]
    assert actual == expected


def test_binary_search_tree_case1():
    node1 = TNode(10)
    node2 = TNode(20)
    node3 = TNode(30)
    node4 = TNode(40)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    bst = BinarySearchTree()
    bst.root = node1
    bst.add(70)
    actual = bst.pre_order()
    expected = [10, 20, 30, 40, 70]
    assert actual == expected


def test_binary_search_tree_case2():
    node1 = TNode(10)
    node2 = TNode(20)
    node3 = TNode(30)
    node4 = TNode(40)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    bst = BinarySearchTree()
    bst.root = node1
    bst.add(90)
    actual = bst.pre_order()
    expected = [10, 20, 30, 40, 90]
    assert actual == expected


def test_binary_search_tree_case3():
    node1 = TNode(10)
    node2 = TNode(20)
    node3 = TNode(30)
    node4 = TNode(40)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    bst = BinarySearchTree()
    bst.root = node1
    bst.add(80)
    actual = bst.post_order(bst.root)
    expected = [20, 80, 40, 30, 10]
    assert actual == expected


def test_binary_search_tree_case4():
    node1 = TNode(10)
    node2 = TNode(20)
    node3 = TNode(30)
    node4 = TNode(40)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    bst = BinarySearchTree()
    bst.root = node1
    bst.add(70)
    actual = bst.in_order()
    expected = [20, 10, 30, 40, 70]
    assert actual == expected


@pytest.fixture
def nodes():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)