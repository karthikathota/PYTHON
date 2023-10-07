Datastrucre is a way of organizing data in a meaningful order.  
We can perform varous operations like inserting items, deleting items, peeking etc.

# STACK

Stack is an Abstact Datatype(ADT).  
It follows Last In First Out(LIFO) mechanism.

### Applications

Undo Redo operations in wordpads.  
Browser back buttons uses stack.  
Backtracking algorithms.  
Stacks can be used in job scheduling algorithms, such as scheduling print jobs in a printer queue.

```PYTHON
max_size=5
top=-1
stack=[None]*max_size #Initializing stack to None with maxsize of 5

def pushitem(x):
    global top #decalring top as a global variable to modify it within the function.
    if(top == max_size-1):
        print("stack is full")
    else:
        top=top+1
        stack[top]=x

def popitem():
    global top #decalring top as a global variable to modify it within the function.
    if(top == -1):
        print("Stack is empty")
    else:
        popped=stack[top]
        print(popped)

```

#QUEUE

Queue is a linear Abstact Datatype(ADT).  
It follows First In First Out(FIFO) rule.  
It posses a major disadvantage i.e to delete an item in the middle of the queue all the items precedding it must be first deleted which causes loss of items. So to overcome this we use circualr queue.

```PYTHON

max_size=5
front = -1
rear = -1
queue=[None]*max_size

def insertitem(x):
    global front
    global rear
    global queue
    if (rear == max_size-1):
        print("Queue is full")
    elif( (rear == -1) and (front == -1)):
        front = 0
        rear = 0
        queue[rear] = x
    else:
        rear = rear + 1
        queue[rear] = x

def deleteitem():
    global front
    global rear
    global queue
    if((rear == -1) and (front == -1)):
        print("Queue is empty no item to be deleted")
    elif( front == rear ):
        deleted = queue[front]
        front = -1
        rear = -1
        print("Last item deleted: ",popped)
    else:
        deleted = queue[front]
        front = front + 1
        print(deleted)
```

# Circular Queue

```PYTHON
max_size=5
front = -1
rear = -1
queue=[None]*max_size

def insertitem(x):
    global front
    global rear
    global queue
    if ((rear + 1) % max_size == front):
        print("Queue is full")
    elif((front == -1) and (rear == -1)):
        front = 0
        rear = (rear + 1) % max_size
        queue[rear] = x
    else:
        rear = (rear + 1) % max_size
        queue[rear] = x

def deleteitem():
    global front
    global rear
    global queue
    if((front == -1) and (rear == -1)):
        print("Queue is empty no item to be deleted")
    elif( front == rear ):
        deleted = queue[front]
        front = -1
        rear = -1
        print(deleted)
    else:
        deleted = queue[front]
        front = (front + 1) % max_size
        print(deleted)



insertitem(1)
insertitem(2)
deleteitem()
```
