# Implement Stack using Queue

from queue import Queue


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0

    def enqueue(self,x):
        self.size += 1
        self.q1.put(x)
    
    def dequeue(self):
        
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
            popped = self.q1.get()
            self.size -= 1
        print(self.q1.get())

s = Stack()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.dequeue()

