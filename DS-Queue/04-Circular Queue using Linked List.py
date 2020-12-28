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

    def front(self):
        if self.is_empty():
            return "Queue empty"
        return self.__front.get_data()

    def enqueue(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.__front=self.__rear=newnode
        else:
            self.__rear.set_next(newnode)
            self.__rear=newnode
        self.__rear.set_next(self.__front)
        self.__length+=1
            
    def dequeue(self):
        if self.is_empty():
            print("nothing to dequeue")
        else:
            nodetodelete=self.__front #for freeing the memory
            itemtodelete=self.__front.get_data()
            if self.__front==self.__rear:
                self.__front=self.__rear=None
            else:
                self.__front=self.__front.get_next()
                self.__rear.set_next(self.__front)
            nodetodelete=None #because in dynamic memory allocation
                              #there is no garbage collection. So we
                              #need to do it manually.
            self.__length-=1
            print(itemtodelete)
        
    def display(self):
        if self.is_empty():
            print("Queue empty, nothing to display")
        else:
            temp=self.__front
            
            while(temp.get_next()!=self.__front):
                print(temp.get_data())
                temp=temp.get_next()
            print(temp.get_data())
            #Another way of displaying elements:-
            '''
            temp=self.__front
            print(temp.get_data())
            temp=temp.get_next()
            while temp != self.__front:
                print(temp.get_data())
                temp=temp.get_next()'''
            
queue=Queue()
queue.enqueue(20)
queue.enqueue(30)
queue.dequeue()
queue.dequeue()
queue.enqueue(50)
queue.enqueue(6)
queue.dequeue()
queue.dequeue()
print(queue.get_sizeof())
print("Queue items are")
queue.display()
#print(queue._Queue__rear.get_data())
