
class Queue:
    def __init__(self,max_size):
        
        self.stack1 = []
        self.stack2 = []
        

    def enqueue(self, data):
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
            
        self.stack1.append(data)

        while len(self.stack2):
            self.stack1.append(self.stack2.pop())
        
        return "added"
    
    def dequeue(self):
        if len(self.stack1) == 0:
           return "Empty queue"
        return self.stack1.pop()

    def __str__(self):
        return str(self.stack1[::-1])

q = Queue(5)
print(q.enqueue(1))
print(q.enqueue(2))

print(q.enqueue(3))
print(q.dequeue())

print(q)




