import pytest
# from linked_list_zip.linked_list_zip import *

from linked_list_zip import *
from code_challenge05.linked_list.linked_list import LinkedList, Node

def test_zip(LL1, LL2):
    actual = zip_lists(LL1, LL2)
    expected = '< 1 > --> < 4 > --> < 2 > --> < 5 > --> < 3 > --> < 6 > --> Null'
    assert actual == expected

def test_zip_one(LL1, LL3):
    actual = zip_lists(LL1, LL3)
    expected = '< 1 > --> < 4 > --> < 2 > --> < 3 > --> Null'
    assert actual == expected

def test_zip_empty(LL1,LL4):
    actual = zip_lists(LL1, LL4)
    expected = str(LL1)
    assert actual == expected

@pytest.fixture
def LL1():
    LL1 = LinkedList()
    LL1.append(1)
    LL1.append(2)
    LL1.append(3)
    return LL1

@pytest.fixture
def LL2():
    LL2 = LinkedList()
    LL2.append(4)
    LL2.append(5)
    LL2.append(6)
    return LL2

@pytest.fixture
def LL3():
    LL3 = LinkedList()
    LL3.append(4)
    return LL3

@pytest.fixture
def LL4():
    LL4 = LinkedList()
    return LL4
