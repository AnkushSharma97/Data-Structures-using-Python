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
        else:
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
        index=self.__top
        while index>=0:
            print(self.__elements[index])
            index-=1
       
class Queue:
    def __init__(self,max_size):
        self.enqueue_stack=Stack(max_size) #Stack1
        self.dequeue_stack=Stack(max_size) #Stack2

    def enqueue(self,data):
        if self.enqueue_stack.is_full():
            print("Queue overflow")
            
        else:
            self.enqueue_stack.push(data)

    def dequeue(self):
        if self.enqueue_stack.is_empty():
            return("Queue empty")
        else:
            #popping items from top from stack1 and pushing it to Stack2
            while not self.enqueue_stack.is_empty():
                data=self.enqueue_stack.pop()
                self.dequeue_stack.push(data)
            itemtodelete=self.dequeue_stack.pop()#item to be deleted from
                                                  #rear of queue.
            #now again putting items back to Stack1 so that we can
            #perform enqueue operation as usual.
            while not self.dequeue_stack.is_empty():
                data=self.dequeue_stack.pop()
                self.enqueue_stack.push(data)
            return itemtodelete
    #since we have done traversing till end in both the queues that is
    #why Complextity=O(n) in dequeue()

    def display(self):
        if self.enqueue_stack.is_empty():
            print("Queue empty")
        else:
            #popping items from top from stack1 and pushing it to Stack2
            print("Queue data from front to rear")
            while not self.enqueue_stack.is_empty():
                data=self.enqueue_stack.pop()
                self.dequeue_stack.push(data)
        self.dequeue_stack.display()
        #Here in display we can directly run display function on Stack1
        #also but then it will diplay items from rear to front but we
        #need it from front to rear and for that at first we will pop all
        #items from stack1 and push it to stack2 and then display stack2.
        #It will give us the items in required order.
        #Complexity= O(n)

queue=Queue(3)
queue.enqueue(40)
queue.enqueue(30)
queue.enqueue(70)
queue.display()






        
