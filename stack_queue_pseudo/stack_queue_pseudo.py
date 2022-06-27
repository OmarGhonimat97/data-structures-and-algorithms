# from stack_and_queue.stack_and_queue import Stack

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

class PseudoQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value):
        self.stack_1.push(value)

    def dequeue(self):
        if self.stack_2.top == None:
            while self.stack_1.top != None:
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()


if __name__ == '__main__':
    stk_1 = PseudoQueue()
    # stk_2 = PseudoQueue()

    stk_1.enqueue(1)
    stk_1.enqueue(2)
    stk_1.enqueue(3)
    # stk_1.enqueue(4)
    print(stk_1.stack_1.top.value)
    # print(stk_1.peek())
    # print(stk_1)

    a = stk_1.dequeue()
    print('a=', a)
    b= stk_1.dequeue()
    print('b=', b)
    c = stk_1.dequeue()
    print('c=', c)
    # d = stk_1.dequeue()
    # print(d)

    # print(str(stk_1))


