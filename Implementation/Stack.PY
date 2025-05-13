class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        print("Printing the stack:-")
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next 
    
    def push(self,value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -=1
        return temp

        
st1 = Stack(1)
st1.push(2)
st1.push(3)
print(st1.pop().value)
st1.print_stack()