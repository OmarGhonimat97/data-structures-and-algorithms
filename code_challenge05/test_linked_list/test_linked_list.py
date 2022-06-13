from linked_list.linked_list import Node, LinkedList
import pytest


def test_node(node):
    assert node


def test_the_value(node):
    assert node.value == 6


def test_the_next(node):
    assert node.next == None


def test_linked_list(ll):
    assert ll


def test_head_value(ll):
    actual = ll.head.value
    expected = 5

    assert actual == expected


def test_the_second_node(ll):
    actual = ll.head.next.value
    expected = 10

    assert actual == expected


def test_str(ll):
    actual = ll.__str__()

    expected = '< 5 > --> < 10 > --> < 15 > --> Null'

    assert actual == expected

def test_insert(LL):
    actual = LL.head.value
    expected = 7
    assert actual == expected

def test_includes_true(LL):
    # actual = LL.head.value
    # expected = True
    # assert actual == expected
    assert LL.includes(7) == True

def test_includes_false(LL):
    assert LL.includes(13) == False

def test_append(LL2):
    actual = LL2.head.next.next.value
    expected = 1
    assert actual == expected

def test_insert_before(LL3):
    actual = LL3.head.next.value
    expected = 8
    assert actual == expected

def test_insert_before_beginning(LL5):
    actual = LL5.head.value
    expected = 9
    assert actual == expected

def test_insert_after(LL4):
    actual = LL4.head.next.next.value
    expected = 8
    assert actual == expected

def test_insert_after_end(LL6):
    actual = LL6.head.next.next.next.value
    expected = 9
    assert actual == expected

@pytest.fixture
def node():
    nod = Node(6)
    return nod


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(15)
    return ll

@pytest.fixture
def LL():
    LL = LinkedList()
    LL.insert(1)
    LL.insert(3)
    LL.insert(5)
    LL.insert(7)
    LL.includes(5)
    return LL

# test append
@pytest.fixture
def LL2():
    LL2 = LinkedList()
    LL2.append(5)
    LL2.append(3)
    LL2.append(1)
    return LL2

# test insert before
@pytest.fixture
def LL3():
    LL3 = LinkedList()
    LL3.append(5)
    LL3.append(3)
    LL3.append(1)
    LL3.insert_before(3, 8)
    return LL3

# test insert before beginning
@pytest.fixture
def LL5():
    LL5 = LinkedList()
    LL5.insert(3)
    LL5.insert(2)
    LL5.insert(1)
    LL5.insert_before(1, 9)
    return LL5


# test insert after
@pytest.fixture
def LL4():
    LL4 = LinkedList()
    LL4.append(5)
    LL4.append(3)
    LL4.append(1)
    LL4.insert_after(3, 8)
    return LL4

# test insert after ending
@pytest.fixture
def LL6():
    LL6 = LinkedList()
    LL6.insert(3)
    LL6.insert(2)
    LL6.insert(1)
    LL6.insert_after(3, 9)
    return LL6