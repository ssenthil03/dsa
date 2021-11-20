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
        self.q = [None]*MAX
        
        self.front = -1
        self.rear = 0

    def isEmpty(self):
        return (self.front == -1)
    
    def isFull(self):
        return ((self.front == 0 and self.rear == self.size-1) or self.front == self.rear + 1)

    def insertFront(self, i):
        if (self.isFull()):
            self.front = 0
            self.rear = 0
        
        elif (self.front == self.size - 1):
            self.front = 0
        else:
            self.front = self.front - 1
        
        self.q[self.front] = i
    
    def deleteFront(self):
        if (self.isEmpty()):
            return
        
        if (self.front == self.rear):
            self.front = -1;
            self.rear = -1;
        else:
            if (self.front == self.size - 1):
                self.front = 0
            else:
                self.front = self.front + 1
        print(self.q)

dec = DQ(10)
dec.insertFront(1)
dec.insertFront(2)
dec.insertFront(3)
dec.insertFront(4)
print(dec.deleteFront())
    

