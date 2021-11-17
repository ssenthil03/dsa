from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        node = Node(data)

        node.next = self.head
        self.head = node
    
    def palindrome(self, head):
        stack = []
        ispalin = True
        while(head is not None):
            stack.append(head.data)

            head = head.next
        while(head is not None):
            value = stack.pop()
            if (head.data == value):
                ispalin = True
            else: 
                ispalin = False
                break
            
            head = head.next
        return ispalin
        

ll = LinkedList()
ll.push(1)
ll.push(0)
ll.push(0)
ll.push(1)

print(ll.palindrome(ll.head))