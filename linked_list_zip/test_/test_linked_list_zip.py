import pytest
from linked_list_zip.linked_list_zip import zip_lists
from code_challenge05.linked_list.linked_list import LinkedList, Node


def test_zip(LL1, LL2):
    actual = LL1.zip_list(LL1, LL2)
    expected = [1, 4, 2, 5, 3, 6]
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