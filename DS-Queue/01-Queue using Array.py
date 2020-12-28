#Queue Implementation using Array:-
#Here we need to consider size factor as well whenever we are doing some
#implementation using array.
#It also leads to various problems like:-(Disadavantages of implementing queue
#using array):-

# 1)Deciding size of array:- The size of Queue can be increased at runtime
#   if required but increasing size of array is a time taking process(because
#   at first it will create new array,then copy all the elements of old array
#   to new one then adds new element which will leads to  O(n) time complexity
#   for every operation of the array) and that is why it is better to know abt
#   our queueue first and then declare the array large enough so that we will
#   not face issue of  new array creation.

# 2)The second problem is, if we overcome the first issue and declare the
#   array large enough, in that case most of our memory spaces which will get
#   acquired by our array in starting will never gets used. In short it will
#   lead to memory wastage.

# 3)Some also says that the one disadvantage is that the dequeue operation
#   deletes element from front of the queue (i.e. deletion from front in array)
#   and due to that internally all shiftings and all things happen so if we
#   declare queue using array then dequeue becomes O(n) but it needs to be O(1)
#   but if we actually look at our code we are not actually removing the values
#   in case of dequeue , we are only incrementing front in that case . (So i dont
#   think it will be a valid limitation)

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__front=-1
        self.__rear=-1

    def is_full(self):
        if self.__rear==self.__max_size-1:
            return True
        return False

    def is_empty(self):
        if self.__rear==self.__front==-1:
            return True
        return False
    
    def front(self):
        if self.is_empty():
            print("Queue is empty")
        return(self.__elements[self.__front])
    
    def enqueue(self,data):
        if self.is_full():
            print("queue overflow")
        elif self.__rear==-1 and self.__front==-1: #or else if is_empty()
            self.__front=self.__rear=0    # or self.__front+=1,self.__rear+=1
            self.__elements[self.__rear]=data
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if self.is_empty():
            print("Queue empty")
        else:
            item=self.__elements[self.__front]
            if self.__front==self.__rear: 
                self.__front=self.__rear=-1
            else:
                self.__front+=1
            return item
        # whenever front and rear are equal then only two things are possible. 
        #1)either the queue is empty. or
        #2)their is only one element in queue.
        #so here first possibiity we have already checked i.e. empty
        #condition in our first loop and if we are inside else and still our
        #rear and front are equal that means there is only one element
        #present in queue.
    def display(self):
        a=[]
        if self.is_empty():
            print("noting to display queue empty")
        else:
            for i in range(self.__front,self.__rear+1):
                print(i)
                a.append(self.__elements[i])
            print(a)
            
            
queue=Queue(5)
queue.display()
element_to_add=["Rahul","Anoop","shivam","komal","anil","raju"]
for i in element_to_add:
    queue.enqueue(i)
print(queue.dequeue())

             
        
        
    
        
        
