''' In this approach we are ging to use single Stack only but we know
recursion also uses stack for its implementation internally. So overall
it will be Two Stacks only i.e. 1 explicit stack + 1 internal stack'''

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.top==self.__max_size-1:
            return True
        return False

    def push(self,data):
        if self.is_full():
            print("Stack overflow, no place for",data)
        else:
            self.top+=1
            self.__elements[self.top]=data

    def is_empty(self):
        if self.top==-1:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            return("stack underflow nothing to pop")
        else:
            temp=self.__elements[self.top]
            self.__elements[self.top]=None
            self.top-=1
            return temp

    def display(self):
        index=0
        while index<=self.top:
            print(self.__elements[index])
            index+=1
global count    
class Queue:
    def __init__(self,max_size):
        self.stack=Stack(max_size) #Stack1

    def enqueue(self,data):
        if self.stack.is_full():
            print("Stack overflow")
        else:
            self.stack.push(data)
            

    def dequeue(self):
        if self.stack.is_empty():
            return("Stack empty")
        elif self.stack.top==0:
            return self.stack.pop()
        value=self.stack.pop()  #here we will pop the value and it will get stored to call stack
        y=self.dequeue()    #do y=self.dequeue()+1 and analyse the result.
        self.stack.push(value)
        return y
                  

    def display(self):
        #there may be many ways to display the elements from front to
        #rear in this code.
        #One way is using the display function of stack but that will
        #print values from top always i.e. it will give values from rear
        #to front.
        
        #another way is using top value and array which stack is using
        #but for this we need the array (self.__elements) to be public
        #so we can follow this approach if our array is public

        #one more way (not optimal) is we can pop the
        #elements from array and store them in some list and then
        #print the list in reverse order.

        #Easisest way is to just change the display code of Stack and
        #make it print values from bottom to top
        if self.stack.is_empty():
            print("Queue empty")
        else:
            print("queye values from front to rear")
            self.stack.display()
            

queue=Queue(4)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
print(queue.dequeue())
queue.display()






        
