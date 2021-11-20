# Implementation of Queue using List

class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.capacity = capacity
        self.rear = self.capacity-1
        self.Queue = [None]*capacity
    
    def isEmpty(self):
        return self.size == 0
    def isFull(self):
        if self.size == self.capacity:
            return True
        return False
    def enqueue(self, x):
        if self.isFull():
            print("Queue is Full !!")
            return -1
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.Queue[self.rear] = x
            self.size = self.size + 1
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue has no elements !!")
            return -1
        else:
            self.front = (self.front + 1) % self.capacity
            self.Queue.remove(self.front)
            self.size = self.size - 1
        return self.Queue

q = Queue(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
