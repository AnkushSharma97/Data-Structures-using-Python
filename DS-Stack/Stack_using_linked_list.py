class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def set_next(self,next):
        self.__next=next

    def get_next(self):
        return self.__next

    def set_data(self,data):
        self.__data=data

    def get_data(self):
        return self.__data

class Stack:
    #1) here we dont take max_size attribute for stack implementation using
    #Linked List because there are no size issues with Linked Lists
    #as compare to Array( like if Array got full then we need
    #to duplicate it and then made new opertaions, so to avoid it we take
    #max_size of stack when we are implementing it with Array and if it goes
    # beyond that size then we simply says "stack overflow" so as to stop
    #duplication process of array as it leads to O(n) complexity.)

    #2) Also it depends on business requirement as well. If it is necessary
    # then we can take max_size attribute into consideration in
    #Stack implementation using Linked List.
    def __init__(self):
        self.__length=0
        self.__top=None
        
    def is_empty(self):
        if self.__top==None:
            return True
        return False

    def get_length(self):
        return self.__length

    def push(self,data):
        #In push operation first work is to check whether stack is full or not
        #i.e. "stack overflow", but because here we are not considering size of
        #stack therefore no need to check for that condition. Or in short
        #"stack size is infinite here due to no size issues in Linked List"
        newnode=Node(data)

        if self.is_empty():
            self.__top=newnode
        else:
            newnode.set_next(self.__top)
            self.__top=newnode
        self.__length+=1


    def pop(self):
        if self.is_empty():
            retun ("stack underflow")

        else:
            popped_element=self.__top
            self.__top=self.__top.get_next()
            popped_element.set_next(None)
            self.__length-=1
            return popped_element.get_data()


    def peek(self):
        return self.__top.get_data()

    def display(self):
        temp=self.__top
        print("Top to Bottom")
        if self.is_empty():
            print("Stack underflow")
            
        else:
            while temp is not None:
                print(temp.get_data())
                temp=temp.get_next()

stack=Stack()
stack.push("Ankush")
stack.push("Sharma")
stack.push("pandey")

stack.pop()
stack.pop()
print(stack.get_length())
stack.display()

        


        
