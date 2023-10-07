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
