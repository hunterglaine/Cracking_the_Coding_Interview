### 3.1 Three in One 


### 3.2 Stack Min
# Design a stack in which in addition to pop() and push() it also has a min()
# method that returns the minimum value of the stack in constant time

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None


    def push(self, new_value):

        self.stack.append(new_value)
        if not self.min:
            self.min = new_value
        elif self.min > new_value:
            self.min = new_value

    
    def pop(self):

        if self.stack:
            self.stack.pop()
            # gone = self.stack.pop()
            # if gone == self.min:

        
    
    def min(self):

        return self.min
