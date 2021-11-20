# Implementation of Singular Linked List.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def push_back(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = node

    def insert(self, data, prev_node):
        node = Node(data)

        node.next = prev_node.next
        prev_node.next = node

    def delete_node(self, data):
        temp = self.head
        while (temp is not None):
            if (temp.data == data):
                break
            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp = None

    def search_node(self, key):
        temp = self.head

        while (temp is not None):
            if (temp.data == key):
                return True
            temp = temp.next
        return False

    def print_mid(self):

        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll.push_front(1)
ll.push_front(2)
ll.push_back(10)
ll.insert(5, ll.head.next)


print("Linked List: ")
ll.printList()
print(f"Whether the element is in the Linked List :{ll.search_node(5)}")

print(ll.print_mid())
