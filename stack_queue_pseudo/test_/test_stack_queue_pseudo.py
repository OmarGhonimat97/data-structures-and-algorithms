import pytest
from stack_queue_pseudo import PseudoQueue, Stack
# from stack_and_queue.stack_and_queue import Stack



def test_enqueue_stack():
    stack = PseudoQueue()
    stack.enqueue(2)
    assert stack.stack_1.top.value == 2

def test_dequeue_stack():
    stack = PseudoQueue()
    stack.enqueue(1)
    stack.enqueue(2)
    stack.enqueue(3)
    assert stack.stack_1.top.value == 3
    stack.dequeue()
    assert stack.stack_2.top.value == 2

# @pytest.fixture
# def pseudo_queue():
#     stack = PseudoQueue()
#     stack.enqueue(1)
#     return stack


