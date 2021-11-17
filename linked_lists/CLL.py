# Implementation of Circular Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLL:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        temp = self.head

        node.next = self.head
        if (self.head is not None):
            while (temp.next != self.head):
                temp = temp.next
            temp.next = node
        else:
            node.next = node
        self.head = node

    def printList(self):
        temp = self.head
        if (self.head is not None):
            while(True):
                print(temp.data)
                temp = temp.next
                if (temp == self.head):
                    break


cll = CircularLL()
cll.push(10)
cll.push(9)
cll.push(8)
cll.push(7)
cll.push(6)
cll.delete(cll.head, 8)
cll.printList()
