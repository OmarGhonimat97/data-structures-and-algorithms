import pytest

# import stack_and_queue.stack_and_queue
from stack_and_queue import Node, Stack, Queue, EmptyStackException, EmptyQueueException

# Stack Tests
def test_node(node):
    assert node

def test_push_stack(stack):
    stack.push(2)
    assert stack.top.value == 2

def test_push_multiple_stack(stack):
    stack.push(3)
    assert stack.top.value == 3
    stack.push(4)
    assert stack.top.value == 4
    stack.push(5)
    assert stack.top.value == 5

def test_pop_stack(stack):
    stack.push(6)
    stack.push(7)
    assert stack.top.value == 7
    stack.pop()
    assert stack.top.value == 6

def test_pop_until_empty(stack):
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.top == None

def test_peek_next_stack(stack):
    stack.push(2)
    assert stack.peek() == 2

def test_instantiating_empty_stack(stack):
    assert stack.top == None

# def test_pop_or_peek_empty_error(stack):
#     actual = stack.pop()
#     expected = pytest.raises(EmptyStackException)
#     assert actual == expected

#Queues Tests
def test_enqueue(queue):
    queue.enqueue(1)
    assert queue.rear.value == 1

def test_multiple_enqueues(queue):
    queue.enqueue(1)
    assert queue.rear.value == 1
    queue.enqueue(2)
    assert queue.rear.value == 2
    queue.enqueue(3)
    assert queue.rear.value == 3

def test_dequeue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1

def test_peek_queue(queue):
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.peek() == 3

def test_empty_queue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.front == None

def test_instantiating_empty_queue(queue):
    assert queue.front == None

# def test_dequeue_or_peek_empty_error(queue):
#     with pytest.raises(Exception) as e:
#         queue.dequeue()
#     assert repr(e) == '<ExceptionInfo EmptyQueueException("dequeue_or_peek from empty queue is_not allowed") tblen=2>'




@pytest.fixture
def node():
    nod = Node(6)
    return nod

@pytest.fixture
def stack():
    stack = Stack()
    return stack

@pytest.fixture
def queue():
    queue = Queue()
    return queue