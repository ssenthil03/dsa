# Implementing Queue using Stack

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        i = 0
        if (len(self.stack1) or len(self.stack2)== 0):
            self.stack1.append(x)
        else:
            for i in self.stack1:
                self.stack2.append(i)
                
                self.stack1.remove(i)
                self.stack2.append(x)
            self.stack1.extend(self.stack2)
        
    def dequeue(self):
        print(self.stack1.pop())
        print(self.stack1)
        


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()


    
        
    
        