class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top==self.__max_size-1:
            return True
        return False

    def push(self,data):
        if self.is_full():
            print("Stack overflow, no place for",data)
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def is_empty(self):
        if self.__top==-1:
            return True
        return False

    def pop(self):
        if self.is_empty():
            return("stack underflow nothing to pop")
        else:
            temp=self.__elements[self.__top]
            self.__elements[self.__top]=None
            self.__top-=1
            return temp
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            index=self.__top
            while index>=0:
                print(self.__elements[index])
                index-=1

    def __str__(self):
        index=self.__top    
        print("stack elements from top to bottom")
        for i in range(index,-1,-1):
            if i==index:
                print(str(self.__elements[i]),'-----> Top')
            elif i==0:
                print(str(self.__elements[i]),'-----> Bottom')
            else:
                print(str(self.__elements[i]))

def remove():
    global clipboard,undo_stack,redo_stack
    data=clipboard[-1]
    clipboard.remove(data)
    undo_stack.push(data)
    print("Data after removal",clipboard)
def undo():
    global clipboard,undo_stack,redo_stack
    if undo_stack.is_empty():
        print("nothing to undo")
    else:
        data=undo_stack.pop()
        redo_stack.push(data)
        clipboard.append(data)
        print("Clipboard after undo",clipboard)
def redo():
    global clipboard,undo_stack,redo_stack
    if redo_stack.is_empty():
        print("nothing to redo")
    else:
        data=redo_stack.pop()
        if data not in clipboard:
            print("Nothing to redo")
        else:
            clipboard.remove(data)
            undo_stack.push(data)
            print("clipboard after redo",clipboard)
            
    
        

clipboard=['A','B',"C","D","E","F"]
undo_stack=Stack(len(clipboard))
redo_stack=Stack(len(clipboard))
remove()
remove()
undo()
redo()
redo()







