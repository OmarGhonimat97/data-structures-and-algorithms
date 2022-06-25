class EmptyStackException(Exception):
  pass

class EmptyQueueException(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
            node = Node(value)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top == None:
            raise EmptyStackException("Pop from empty stack is not allowed")

        temp = self.top
        self.top = temp.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.top == None:
            raise EmptyStackException("Peek from empty stack is not allowed")
        else:
            return self.top.value

    def is_empty(self):
        return True if self.top == None else False

    def __str__(self):
        current = self.top
        items = ''

        while current:
            items += str(current.value) + '\n'
            current = current.next

        return items

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



    def __str__(self):
        current = self.front
        items = ''

        while current:
            items += str(current.value) + '\n'
            current = current.next

        return items



if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    # print(stack.is_empty())
    # stack.pop()
    # print(stack.peek())
    # print(str(stack))

    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    # print(queue.peek())
    print(queue.is_empty())

    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    # print(queue)