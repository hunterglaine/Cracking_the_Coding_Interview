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


### 3.3 Stack of Plates
# Implement a data structure, StackOfStacks, composed of several stacks that creates a new stack when
# the previous stack exceeds capacity. It should have a push() and pop() method that returns the same
# type of values as a singular stack would

class StackOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, value):
        if self.stacks:
            if len(self.stacks[-1]) < self.capacity:
                self.stacks[-1].append(value)
            else:
               self.stacks.append([value]) 
        else:
            self.stacks.append([value])

    def pop(self):
        if self.stacks:
            popped = self.stacks[-1].pop()
            if not self.stacks[-1]:
                self.stacks.pop()
            return popped


### 3.4 Queue via Stacks
# Implement a MyQueue class which implements a queue using two stacks.

# queue should have pop from front, push to end, peek at first item, 
class MyQueue:
    def __init__(self):
        self.pop_peek_lst = []
        self.push_lst = []

    def push(self, value):
        self.push_lst.append(value)
    
    def pop(self):
        if not self.pop_peek_lst:
            if self.push_lst:
                self.push_lst.reverse()
                self.pop_peek_lst = self.push_lst
                self.push_lst = []
            else:
                return
        return self.pop_peek_lst.pop()

    def peek(self):
        if not self.pop_peek_lst:
            if self.push_lst:
                return self.push_lst[0]
            else:
                return
        else:
            return self.pop_peek_lst[-1]

