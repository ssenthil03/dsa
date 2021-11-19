# Implementation of Stack to find mid element with O(1) Complexity

class DLL:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None
    
class Stack:
    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0

def createMyStack():
    ms = Stack()
    ms.count = 0
    return ms

def push(ms, x):
    node = DLL(x)
    
    node.prev = None
    node.next = ms.head

    ms.count += 1
    if (ms.count == 1):
        ms.mid = node
    else:
        ms.head.prev = node

        if ((ms.count % 2) != 0):
            ms.mid = ms.mid.prev
    ms.head = node

def pop(ms):
    if (ms.count == 0):
        return
    
    head = ms.head
    item = ms.head.data
    ms.head = head.next

    if (ms.head != None):
        ms.head.prev = None
    ms.count -= 1

    if ((ms.count % 2) == 0):
        ms.mid = ms.mid.next
    return item

def findMiddle(ms):
    if (ms.count == 0):
        print("Stack is Empty")
    return ms.mid.data



ms = createMyStack()
push(ms, 1)
push(ms, 2)
push(ms, 3)
push(ms, 4)
print(pop(ms))
print(str(findMiddle(ms)))

    
        
    

