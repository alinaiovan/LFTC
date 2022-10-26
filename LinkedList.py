from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


    def add(self, newData):
        NewNode = Node(newData)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while laste.next:
            laste = laste.next
        laste.next = NewNode

    def __str__(self):
        return '\n'.join([str(node) for node in self])
