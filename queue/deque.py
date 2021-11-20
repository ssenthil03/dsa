''' Implementation of Deque (Double Ended Queue)
    that means elements can be inserted and deleted at both ends of the
    queue  
    
    insertFront() => inserts the element at the front of the queue
    insertRear() => inserts the element at the end of the queue
    deleteFront() => deletes the element at the front of the queue
    deleteRear() => deletes the element at the rear of the queue

    getFront() => gets the element at the first of the queue
    getRear() => gets the element at the end of the queue

    This methods can be implemented by Circular Array
    
    '''
MAX = 100
class DQ:
    def __init__(self, size):
        self.size = size
        self.q = [None]*size
        
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return (self.front == -1)
    
    def isFull(self):
        return ((self.front == 0 and self.rear == self.size-1) or self.front == self.rear + 1)

    def insertFront(self, i):
        if (self.isFull()):
            print("Overflow")
            return
        
        if (self.front == -1):
            self.front = 0
            self.rear = 0
        elif (self.front == 0):
            self.front = self.size - 1
        else:
            self.front -= 1
        self.q[self.front] = i
    
    def insertRear(self, i):
        if (self.isFull()):
            self.front = 0
            self.rear = 0
            self.q[self.rear] = i
        elif (self.rear == self.size - 1):
            self.rear = 0
            self.q[self.rear] = i
        else:
            self.rear = self.rear + 1
            self.q[self.front] = i
        
    
    def deleteFront(self):
        if (self.isEmpty()):
            print("The Deque is Empty !!")
            return
        
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            if (self.front == self.size - 1):
                self.front = 0
            else:
                self.front = self.front + 1
    
    def deleteRear(self):
        if (self.isEmpty()):
            return
        
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            if (self.rear == self.size - 1):
                self.rear = self.rear - 1
            else:
                self.rear = self.size - 1

    def getFront(self):
        return self.q[self.front]

    def getRear(self):
        return self.q[self.rear]

    

dec = DQ(10)
dec.insertFront(1)
dec.insertFront(2)
dec.insertFront(3)
dec.insertFront(4)
dec.deleteFront()

    

