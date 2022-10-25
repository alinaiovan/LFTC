from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, newData):
        NewNode = Node(newData)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while laste.next:
            laste = laste.next
        laste.next = NewNode

    def list(self):
        printval = self.head
        while printval is not None:
            print(printval.val)
            printval = printval.next
