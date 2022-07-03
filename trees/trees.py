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

    # def pre_order_iter(self):
    #     if not self.root:
    #         return self.root
    #
    #     stack = Stack()
    #     stack.push(self.root)
    #
    #     while not stack.is_empty():
    #         top = stack.pop()
    #         print(top.value)
    #
    #         if top.right:
    #             stack.push(top.right)
    #
    #         if top.left:
    #             stack.push(top.left)

    def post_order(self, root):
        output = []
        if root:
            output = self.post_order(root.left)
            output = output + self.post_order(root.right)
            output.append(root.value)
        return output

    # def post_order(self):
    #     output = []
    #     if not self.root:
    #         return self.root
    #
    #     def _walk(root):
    #
    #         if root:
    #             output = self._walk(root.left)
    #             output = output + self._walk(root.right)
    #             output.append(root.value)
    #         return output
    #
    #     _walk(self.root)
    #     return output



class BinarySearchTree(BinaryTree):

    def add(self, value):
        """
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
        """
        if not self.root:
            self.root = TNode(value)

        def _walk(root):
            if value < root.value:
                if root.left:
                    _walk(root.left)
                else:
                    root.left = TNode(value)
            elif value > root.value:
                if root.right:
                    _walk(root.right)
                else:
                    root.right = TNode(value)

        _walk(self.root)

    def contains(self, value):
        """
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        """

        current = self.root

        while True:
            if current.value == value:
                return True

            if current.left and value < current.value:
                current = current.left
            elif current.right and value > current.value:
                current = current.right
            else:
                break

        return False


if __name__ == "__main__":
    tree = BinaryTree()
    # tree.root = TNode(10)
    # tree.root.left = TNode(20)
    # tree.root.right = TNode(50)
    # tree.root.left.left = TNode(30)
    # tree.root.left.right = TNode(40)
    # tree.root.right.left = TNode(60)

    print(tree.breadth_first())
    tree.pre_order()

    tree = BinaryTree()
    tree.root = TNode(1)
    tree.root.left = TNode(2)
    tree.root.right = TNode(3)
    tree.root.left.left = TNode(4)
    tree.root.left.right = TNode(5)
    tree.root.right.left = TNode(6)
    print(" pre order ")
    print(tree.pre_order())
    print("in order")
    print(tree.in_order())
    print("post order ")
    print(tree.post_order(tree.root))

    # bst = BinarySearchTree()
    # bst.add(10)
    # bst.add(20)
    # bst.add(30)
    # bst.add(40)
    # print(bst.pre_order())
