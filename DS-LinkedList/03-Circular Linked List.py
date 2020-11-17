class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    def get_data(self):
        return self.__data
    def get_next(self):
        return self.__next
    def set_data(self,data):
        self.__data=data
    def set_next(self,next):
        self.__next=next

class Circularlinkedlist:
    def __init__(self):
        self.__head=None
        self.__tail=None
    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail

    def add(self,data):
        newNode=Node(data)
        if self.__head is None:
            self.__head=self.__tail=newNode
        else:
            self.__tail.set_next(newNode)
            self.__tail=newNode
            newNode.set_next(self.__head)
    def display(self):
        print(self.__head.get_data())
        temp=self.__head.get_next()
        while temp != self.__head:
            print(temp.get_data())
            temp=temp.get_next()

clist=Circularlinkedlist()
clist.add(32)
clist.add(34)
clist.add(32)
clist.add(45)
clist.display()
print(clist.get_head().get_data(),clist.get_tail().get_data())
