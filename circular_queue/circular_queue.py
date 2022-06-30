class EmptyQueueException(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front == None:
            raise EmptyQueueException("dequeue_or_peek from empty queue is_not allowed")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        if self.front == None:
            raise EmptyQueueException("dequeue_or_peek from empty queue is_not allowed")
        else:
            return self.front.value

    def is_empty(self):
        return True if self.front == None else False

    # def __str__(self):
    #     current = self.front
    #     items = ''
    #
    #     while current:
    #         items += str(current.value) + '\n'
    #         current = current.next
    #
    #     return items


def duck_duck_goose(input_string, k):
    if not input_string:
        return "Empty input string"

    my_str = list(input_string)

    queue = Queue()
    for i in my_str:
        queue.enqueue(i)

    queue.rear.next = queue.front

    while queue.rear.value != queue.front.value:

        for i in range(k - 1):
            queue.front = queue.front.next
            queue.rear = queue.rear.next

        queue.dequeue()
        queue.rear.next = queue.front
    return queue.front.value




if __name__ == '__main__':
    print(duck_duck_goose("ABCDE", 3))

    print(duck_duck_goose("EDCBA", 3))

    print(duck_duck_goose("A", 3))
    print(duck_duck_goose("", 3))

    print(duck_duck_goose("ABCDE", 2))