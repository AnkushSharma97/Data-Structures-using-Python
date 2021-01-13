class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
        self.__prev=None

    def get_data(self):
        return self.__data

    def set_prev(self,prev_node):
        self.__prev=prev_node

    def set_next(self,next_node):
        self.__next=next_node

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

class Deque:
    def __init__(self):
        self.__front=None
        self.__rear=None

    def is_empty(self):
        if self.__front==None and self.__rear==None:
            return True
        return False

    def insert_rear(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.__front=self.__rear=new_node
        else:
            self.__rear.set_next(new_node)
            new_node.set_prev(self.__rear)
            self.__rear=new_node

    def insert_front(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.__front=self.__rear=new_node
        else:
            new_node.set_next(self.__front)
            self.__front.set_prev(new_node)
            self.__front=new_node

    def delete_front(self):
        if self.is_empty():
            print("Deque already empty")
        else:
            data=self.__front.get_data()
            if self.__front==self.__rear:
                self.__front=self.__rear=None
            else:
                self.__front=self.__front.get_next()
                self.__front.set_prev(None)
            return data
        
    def delete_rear(self):
        if self.is_empty():
            print("Deque already empty")
        else:
            data=self.__rear.get_data()
            if self.__front==self.__rear:
                self.__front=self.__rear=None
            else:
                self.__rear=self.__rear.get_prev()
                self.__rear.set_next(None)
            return data

    def display(self):
        if self.is_empty():
            print("Deque already empty")
        else:
            temp=self.__front
            while temp is not None:
                print(temp.get_data())
                temp=temp.get_next()
    
            
deck=Deque()
deck.insert_rear(34)
deck.insert_rear(39)
deck.insert_rear(49)
deck.insert_front(499)
deck.insert_front(69)
deck.delete_front()
deck.delete_rear()
deck.delete_front()
deck.display()

