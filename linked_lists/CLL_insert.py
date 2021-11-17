# Implementation of Circular Linked List Insertion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.last = None

    def insert_begin(self, data):

        node = Node(data)

        if (self.last is None):
            self.last = node
            node.next = self.last

        else:
            temp = self.last.next
            self.last.next = node
            node.next = temp
        return self.last

    def insert_end(self, data):
        node = Node(data)
        if(self.last is None):
            node.next = self.last
            self.last = node
        else:
            temp = self.last.next
            self.last.next = node
            node.next = temp
            self.last = node
        return self.last

    def insert_at_pos(self, prev, data):
        node = Node(data)
        if (self.last is None):
            node.next = self.last
            self.last = node
        else:
            temp = self.last.next

    def insert_after(self, data, item):
        node = Node(data)
        cur = self.last.next

        while cur:
            if (cur.data == item):
                node.next = cur.next
                cur.next = node

                if(cur == self.last):
                    self.last = node
                    return self.last
                else:
                    return self.last
            cur = cur.next

            if (cur == self.last.next):
                print(f"{item} is not present in the linked list")
                break

    def printList(self):
        temp = self.last.next
        while(temp):
            print(temp.data)
            temp = temp.next
            if (temp == self.last.next):
                break


cll = CLL()
cll.insert_begin(10)
cll.insert_begin(12)
cll.insert_begin(11)
cll.insert_end(13)
cll.insert_after(14, 11)
cll.printList()
