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
            raise EmptyQueueException("Empty Queue, you can't dequeue from")
        else:
            temp_node = self.front
            self.front = self.front.next
            return temp_node.value

    def is_empty(self):
        return False if self.front else True


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Takes the vlaue and make a node and append it to the top of the stack
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def is_empty(self):
        return False if self.top else True

    def pop(self):
        if self.is_empty():
            raise Exception
        """
        a method to pop the top value of the stack
        input: no input
        output:
        the value popped from the stack
        """
        temp = self.top.value
        self.top = self.top.next
        return temp


class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class KTee():
    pass


class BinaryTree:
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

            if front.left:
                queue.enqueue(front.left)

            if front.right:
                queue.enqueue(front.right)

        return output

    def pre_order(self):
        output = []
        if not self.root:
            return self.root

        def _walk(root):
            output.append(root.value)

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def in_order(self):

        output = []
        if not self.root:
            return self.root

        def _walk(root):

            if root.left:
                _walk(root.left)

            output.append(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def post_order(self, root):
        output = []
        if root:
            output = self.post_order(root.left)
            output = output + self.post_order(root.right)
            output.append(root.value)
        return output

    # def max_value(self, root):
    #     if not root:
    #         return root
    #
    #     max_val = root.value
    #     left_max = self.max_value(root.left)
    #     right_max = self.max_value(root.right)
    #
    #     if left_max > max:
    #         max_val = left_max
    #     if right_max > max:
    #         max_val = right_max
    #     return max_val

    def max_value(self):
        if not self.root:
            return self.root

        def _walk(root):
            if root == None:
                return -9999999
            max_val = root.value
            left_max = _walk(root.left)
            right_max = _walk(root.right)

            if left_max > max_val:
                max_val = left_max
            if right_max > max_val:
                max_val = right_max
            return max_val
        return _walk(self.root)



    # def max_value(self):
    #     if not self.root:
    #         return self.root
    #     # max_val = self.root.value
    #
    #     def _walk(root):
    #         # output.append(root.value)
    #
    #         if root.value > max_val:
    #             max_val = root.value
    #
    #         if root.left:
    #             _walk(root.left)
    #
    #         if root.right:
    #             _walk(root.right)
    #     _walk(self.root)
    #     return max_val


if __name__ == "__main__":

    tree = BinaryTree()
    tree.root = TNode(1)
    tree.root.left = TNode(2)
    tree.root.right = TNode(5)
    tree.root.left.left = TNode(3)
    tree.root.left.right = TNode(4)
    tree.root.right.left = TNode(6)

    print(tree.breadth_first())

    print(tree.max_value())