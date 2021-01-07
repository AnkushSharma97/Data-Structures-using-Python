class Deque:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__deque=[None]*max_size
        self.__front=-1
        self.__rear=-1

    def is_empty(self):
        if self.__front==-1 and self.__rear==-1:
            return True
        return False

    def is_full(self):
        if (self.__front==self.__rear+1) or (self.__front==0 and self.__rear==self.__max_size-1):
             return True
        return False
    
    ''' or for checking full we can simply add circular queue full condition
        as well i.e. if (rear+1% max_size)==front then True else False'''


    def insert_rear(self,data):
        if self.is_full():
            print("Queue overflow")
        else:
            if self.is_empty():
                self.__front=self.__rear=0
                
            elif self.__rear==self.__max_size-1:
                self.__rear=0
                
            else:
                self.__rear+=1
        self.__deque[self.__rear]=data

    ''' we can also implement insert_rear() in the same way we have used
        enqueue() function in Circular Queue i.e. by using modulus '''

    def insert_front(self,data):
        if self.is_full():
            print("Queue overflow")
        else:
            if self.is_empty():
                self.__front=self.__rear=0
                
            elif self.__front==0:
                self.__front=self.__max_size-1
                
            else:
                self.__front-=1
            self.__deque[self.__front]=data

    def delete_front(self):
        if self.is_empty():
            print("queue empty")
        else:
            itemtodelete=self.__deque[self.__front]
            if self.__front==self.__rear:
                self.__front=self.__rear=-1
            elif self.__front==self.__max_size-1:
                self.__front=0
            else:
                self.__front+=1
            return itemtodelete

    ''' we can also implement it in the same way we have used dequeue() func
        in Circular queue i.e. by using modulus'''

    def delete_rear(self):
        if self.is_empty():
            print("queue empty")
        else:
            itemtodelete=self.__deque[self.__rear]
            if self.__front==self.__rear:
                self.__front=self.__rear=-1
            elif self.__rear==0:
                self.__rear=self.__max_size-1
            else:
                self.__rear-=1
            return itemtodelete

    def get_front(self):
        if self.is_empty():
            print("queue empty")
        else:
            print(self.__deque[self.__front])

    def get_rear(self):
        if self.is_empty():
            print("queue empty")
        else:
            print(self.__deque[self.__rear])

    def display(self):
        temp=self.__front
        print("Deque elements from front to rear are as follows:- ")
        while temp!=self.__rear:
            print(self.__deque[temp])
            temp=(temp+1)%self.__max_size
        print(self.__deque[temp])
    def __str__(self):
        return(str(self.__deque))
                

deck=Deque(5)
deck.insert_front(37)
deck.insert_front(45)
deck.insert_front(26)
deck.insert_rear(23)
deck.delete_front()

deck.insert_front(28)
print(deck.delete_rear())
deck.insert_rear(22)
deck.get_rear()
deck.display()
print(deck)

                
