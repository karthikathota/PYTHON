# STACK

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
