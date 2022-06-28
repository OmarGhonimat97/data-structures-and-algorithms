import pytest
from stack_queue_animal_shelter import *

def test_enqueue_cat():
    queue = AnimalShelter()
    queue.enqueue('Grace', 'CAt')
    assert queue == {"name": 'Grace', "type": "cat"}






# @pytest.fixture
# def queue_stack():
#     queue = AnimalShelter()
#     return queue