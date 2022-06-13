class Node:
    """
  It will store the data and the reference to next node
  """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
  It will have a sequence of nodes
  """
    def __init__(self):
        self.head = None

    def append(self, value):
        """
    It will add a node to the end of the linked list

    parameters : Value
    return: Nothing
    """
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next

    #   current.next = Node(value)
            current.next = new_node

    def insert(self, value):
        """
        inserting the node at the beginning of the linked list
        """
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def includes(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    def insert_before(self, value, new_value):
        """
        inserts a new node before a given node
        """
        if self.includes(value):
            current = self.head
            if current.value == value:
                new_node = Node(new_value)
                new_node.next = current
                self.head = new_node
            else:
                while current.next:
                    if current.next.value == value:
                        new_node = Node(new_value)
                        new_node.next = current.next
                        current.next =new_node
                        break
                    current = current.next

    def insert_after(self, value, new_value):
        """
        inserts a new node after a given node
        """
        if self.includes(value):
            current = self.head
            while current:
                if current.value == value:
                    new_node = Node(new_value)
                    new_node.next = current.next
                    current.next = new_node
                    break
                elif current.next == None:
                    new_node = Node(new_value)
                    current.next = new_node
                current = current.next

    def __str__(self):
        current = self.head
        items = ''
        while current:
            items += f"< {current.value} > --> "
            current = current.next
        items += "Null"
        return items


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.insert(15)
    print(ll.includes(5))
    # print(ll.head.value)
    # print(ll.head.next.value)
    # ll.insert_before(5, 8)
    ll.insert_after(5, 8)

    print(ll)



