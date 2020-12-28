#Circular Queue implementation.
#this implementation is possible using array only because we dont have
#any size or Array full type of issue in Linked List implementation.

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__front=-1
        self.__rear=-1

    def is_full(self):
        if (self.__rear+1)%self.__max_size ==self.__front:
            return True
        return False
        
    def is_empty(self):
        if self.__front==-1 and self.__rear==-1:
            return True
        return False
    def front(self):
        if is_empty(self):
            print("Queueu empty")
        else:
            return self.__elements[self.__front]
        
    def enqueue(self,data):
        if self.is_full():
            print("Queue Full")
        elif self.is_empty():
            self.__rear=self.__front=0
            self.__elements[self.__rear]=data
        else:
            self.__rear=(self.__rear+1)% self.__max_size
            self.__elements[self.__rear]=data
            
    def dequeue(self):
        if self.is_empty():
            print("Queue already empty")
        else:
            itemtodelete=self.__elements[self.__front]
            if self.__front==self.__rear:
                self.__front=self.__rear=-1
            else:
                self.__front=self.__front+1%self.__max_size
            return itemtodelete
            
        
    def display(self):
        if self.is_empty():
            print("Queue empty")
        else:
            temp=self.__front
            while(temp != self.__rear):
                print(self.__elements[temp])
                temp= (temp+1) % self.__max_size
            print(self.__elements[temp])


queue=Queue(3)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.dequeue()
queue.dequeue()
queue.enqueue(80)
queue.enqueue(60)
queue.enqueue(59)
queue.display()
