class EmptyQueueException:
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
        """
        It will insert a node to the queue
        """
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            raise EmptyQueueException("Empty Queue, you can't dequeue")
        else:
            temp_node = self.front
            self.front = self.front.next
            return temp_node.value

    def is_empty(self):
        return False if self.front else True


class KTNode:
    def __init__(self, value):
        self.value = value
        self.children = []


class KArrTree:
    def __init__(self):
        self.root = None

    def breadth_first(self):
        if not self.root:
            return self.root
        output = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            front = queue.dequeue()
            output.append(front.value)

            for child in front.children:
                queue.enqueue(child)

        return output


def fizz_buzz_tree(k_ary_tree):

    def _walk(root):
        if not root:
            return root
        output = []
        queue = Queue()
        queue.enqueue(root)

        while not queue.is_empty():
            front = queue.dequeue()
            # output.append(front.value)
            if front.value % 3 == 0 and front.value % 5 == 0:
                output.append('FizzBuzz')
            elif front.value % 3 == 0:
                output.append('Fizz')
            elif front.value % 5 == 0:
                output.append('Buzz')
            else:
                output.append(f'{front.value}')

            for child in front.children:
                queue.enqueue(child)

        return output

    return _walk(k_ary_tree.root)


# def fizz_buzz_tree(k_ary_tree):
#     output = []
#     for i in k_ary_tree:
#         if i % 3 == 0 and i % 5 == 0:
#             output.append('FizzBuzz')
#         elif i % 5 == 0:
#             # i = 'Buzz'
#             output.append('Buzz')
#         elif i % 3 == 0:
#             # i = 'Fizz'
#             output.append('Fizz')
#         else:
#             output.append(str(i))
#             # i = str(i)
#
#     return output

if __name__ == "__main__":
    tree = KArrTree()
    tree.root = KTNode(1)
    # tree.root.children = KTNode([2, 3, 4])
    tree.root.children.append(KTNode(2))
    tree.root.children.append(KTNode(3))
    tree.root.children[0].children.append(KTNode(15))
    tree.root.children[1].children.append(KTNode(20))

    print(tree.breadth_first())

    print(fizz_buzz_tree(tree))