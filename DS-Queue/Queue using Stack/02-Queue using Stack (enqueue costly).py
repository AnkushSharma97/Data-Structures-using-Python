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
        if self.dequeue_stack.is_full():
            print("Queue overflow")
        else:
            while not self.dequeue_stack.is_empty():
                popped_data=self.dequeue_stack.pop()
                self.enqueue_stack.push(popped_data)
            self.enqueue_stack.push(data)

            while not self.enqueue_stack.is_empty():
                popped_data=self.enqueue_stack.pop()
                self.dequeue_stack.push(popped_data)

        #Complexity= O(2n) or O(n)
            

    def dequeue(self):
        if self.dequeue_stack.is_empty():
            print("Queue empty")
        else:
            print("item popped is",self.dequeue_stack.pop())
        #Complexity=O(1)

    def display(self):
        if self.dequeue_stack.is_empty():
            print("Queue empty")
        else:
            self.dequeue_stack.display()
        #Complexity=O(n)
            

queue=Queue(3)
queue.enqueue(40)
queue.enqueue(30)
queue.enqueue(70)
queue.enqueue(50)
queue.dequeue()
queue.display()






        
