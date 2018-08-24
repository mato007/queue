class Queue:


    def __init__(self,size):
        self.size = size
        self.Q = [0] * size
        self.num = 0
        self.first = 0

    def enqueue(self, item):
        if self.num >= self.size:
            raise Exception("INVALID")
        self.Q[self.num+self.first%self.size] = item
        self.num += 1

    def dequeue(self):
        if self.num == 0:
            raise Exception("Queue empty")
        item = self.Q[self.first]
        self.first = (self.first + 1) % self.size
        self.num -= 1
        return item

    def front(self):
        if self.num == 0:
            raise Exception("Queue empty")
        return self.Q[self.first]


    def is_empty(self):
        return self.num == 0

    def size(self):
        return self.num

    def is_full(self):
        return self.num >= self.size

q=Queue(10) # (front of queue)[](back of queue)
q.enqueue("ra'na") # ["ra'na"]
q.enqueue("vez") # ["ra'na", "vez"]
q.enqueue("Arya") # ["ra'na", "vez", "Arya"]
#print("queue size is: ",q.size())
print(q.dequeue(), "left the queue") # ["vez", "Arya"]
print("front of queue is:",q.front())
q.enqueue("milda") # ["vez", "Arya", "milda"]
q.dequeue() # ["Arya","milda"]
q.dequeue() # ["milda"]
q.dequeue() # []
print("It was a queue")
