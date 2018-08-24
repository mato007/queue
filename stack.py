class Stack:

    def __init__(self,size):
        self.size = size
        self.S = [0] * size
        self.num = 0


    def push(self,item):

        if self.num >= self.size:
            raise Exception("Stack overflow")
        self.S[self.num] = item
        self.num += 1

    def pop(self):
        if self.num == 0:
            raise Exception("Stack empty")
        self.num -= 1
        return self.S[self.num]


    def top(self):
        if self.num == 0:
            raise Exception("Stack empty")
        return self.S[self.num-1]


    def size(self):
        return self.num

    def is_full(self):
        return self.num >= self.size

    def is_empty(self):
        return self.num == 0



st=Stack(10) # (top of stack)[]
st.push(10) # [10]
st.push(30) # [30, 10]
st.push(10) # [1.5, 30, 10]
print(st.pop()," is popped") # [30, 10]
st.push("salam") # ["salam", 30, 10]
st.pop() # [30, 10]
print("Top of stack: ",st.top())
st.pop() # [10]
st.pop() # []
print("Stack is empty: ",st.is_empty())

