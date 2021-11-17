class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        temp = self.head
        if (self.head is None):
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
        else:
            while(temp.next is not None):
                temp = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            temp.next = new_node

    def printList(self):
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp = temp.next


dll = DLL()
dll.push(1)
dll.push(2)
dll.push(3)
dll.push(4)
dll.printList()
