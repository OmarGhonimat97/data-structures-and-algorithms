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



    def __str__(self):
        current = self.front
        items = ''

        while current:
            items += str(current.value) + '\n'
            current = current.next

        return items



class AnimalShelter(object):
    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, name, pref):
        animal = {
            "name": name,
            "type": pref
        }
        if pref == "dog":
            self.dogs.append(animal)
        elif pref == "cat":
            self.cats.append(animal)
        else:
            print("Invalid animal type")


    def dequeue(self, pref):
        if pref == "dog":
            return self.dogs.pop()
        elif pref == "cat":
            return self.cats.pop()
        else:
            return None





if __name__ == '__main__':
    pass
