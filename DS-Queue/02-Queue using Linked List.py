class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
        
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
        
    def get_next(self):
        return self.__next
    
    def set_next(self,next):
        self.__next=next

class Queue:
    def __init__(self):
        self.__length=0 #for getting size of Queue
        self.__front=None
        self.__rear=None

    def get_sizeof(self):
        return self.__length

    def is_empty(self):
        if self.__rear==None and self.__front==None:
            return True
        return False

    #no need for is_full() becoz there is no size limit in Linked List
    #implementation.

    def front(self):
        if self.is_empty():
            return "Queue empty"
        return self.__front.get_data()

    def enqueue(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.__front=self.__rear=new_node
        else:
            self.__rear.set_next(new_node)
            self.__rear=new_node    #self.__rear=self.__rear.get_next()
        self.__length+=1
            
    def display(self):
        if self.is_empty():
            print("queue is empty")
        else:
            temp=self.__front
            print("Queue data from front to rear")
            while temp is not None:
                print(temp.get_data(), end=" ")
                temp=temp.get_next()
            print()

    def dequeue(self):
        if self.is_empty():
            print("nothing to delete")
        else :
            temp=self.__front # line1
            itemtodelete=self.__front.get_data()
            if self.__front==self.__rear:
                self.__front=None
                self.__rear=None
            else:
                self.__front=self.__front.get_next()
            temp=None # this is just to ensure that the  memory occupied by old
                      #front gets freed. Because there is no automatic garbage
                      #collector in dynamic memory allocation(not sure that this is
                      #in python as well or not). That is why we took temp in line 1.
            print(itemtodelete)
            self.__length-=1

queue=Queue()
print(queue.is_empty())
queue.enqueue(56)
queue.enqueue(65)
queue.enqueue(87)
queue.enqueue(67)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()
print(queue.is_empty())

queue.display()
print(queue.get_sizeof())




    
