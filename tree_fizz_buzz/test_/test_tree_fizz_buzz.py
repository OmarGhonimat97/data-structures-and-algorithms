import pytest
from tree_fizz_buzz import *


def test_empty_k_ary_tree():
    tre = KArrTree()
    assert tre.root is None

def test_k_ary_tree():
    tre = KArrTree()
    tre.root = KTNode(1)
    tre.root.children.append(KTNode(2))
    tre.root.children.append(KTNode(3))
    tre.root.children.append(KTNode(4))
    tre.root.children[0].children.append(KTNode(10))
    tre.root.children[0].children.append(KTNode(15))
    tre.root.children[0].children.append(KTNode(20))
    actual = tre.breadth_first()
    expected = [1, 2, 3, 4, 10, 15, 20]
    assert actual == expected

def test_k_ary_fizz_buzz():
    tre = KArrTree()
    tre.root = KTNode(1)
    tre.root.children.append(KTNode(2))
    tre.root.children.append(KTNode(3))
    tre.root.children.append(KTNode(4))
    tre.root.children[0].children.append(KTNode(10))
    tre.root.children[0].children.append(KTNode(15))
    tre.root.children[1].children.append(KTNode(20))
    actual = fizz_buzz_tree(tre)
    expected = ['1', '2', 'Fizz', '4', 'Buzz', 'FizzBuzz', 'Buzz']
    assert actual == expected


