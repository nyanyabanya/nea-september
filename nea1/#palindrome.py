

class Stack():
    def __init__(self):
        self.list=["","","","",""]
        self.rear=0
        self.front=0
        self.max=5
        self.size=0

    def isFull(self):
        if self.size==(self.max):
            return True

    def push(self,x):
            self.list[self.rear]=x
            self.rear+=1
            self.size+=1

    def pop(self):
        self.list.pop()
        self.size+=-1
        self.rear+=-1
        return self.rear

    
    def isEmpty(self):
        if self.front==self.rear:
            return True
        else:
            return False

    def peak(self):
        print(self.list)

    def size(self):
        return (self.size)
s=Stack()
print(s.isEmpty())
s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.push("E")
print(s.isFull())
s.pop()
s.peak()
print(s.isEmpty())

