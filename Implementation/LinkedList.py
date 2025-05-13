class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def preppend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    def printlist(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next
            
    def pop(self):
        if self.length == 0:
            print("Linked List is empty")
            return None

        temp = self.head

        if self.length == 1:
            print(temp.value)
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        prev = self.head
        curr = self.head.next
        while curr.next is not None:
            prev = curr 
            curr = curr.next

        print(curr.value)
        prev.next = None
        self.tail = prev
        self.length -= 1
        return curr

    
    def pip(self):
        if self.length == 0:
            print("Linked List is empty")

        temp = self.head

        if self.length == 1:
            print(temp.value)
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        
        print(temp.value)
        self.head = temp.next
        self.length -= 1
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self,index,value):
        if index == 0:
            self.preppend(value)
        if index == self.length-1:
            self.append(value)
        
        new_node = Node(value)
        prev = self.get(index-1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            print("Index Out Of Range")
            return None
        if index == 0:
            self.pip()
        if index == self.length-1:
            self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def find_middle_node(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        pass
ll1 = LinkedList(1)
# print(ll1.length)
# print(ll1.head.next.value)
print("-----------")
ll1.append(6)
ll1.append(2)
ll1.append(8)
ll1.append(9)
print(ll1.find_middle_node().value)