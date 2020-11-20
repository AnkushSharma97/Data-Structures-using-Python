class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None #points to a node or in short it is also a node

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return(self.__next)

    def set_next(self,next):
        self.__next=next
        
class LinkedList:
    def __init__(self):
        self.__head=None    #head Node (here it is just a common variable)
        self.__tail=None    #tail Node (here it is just a common variable)
    def get_head(self):
        return self.__head
    def set_head(self,head):
        self.__head=head
    def set_tail(self,tail):
        self.__tail=tail
    def get_tail(self):
        return self.__tail
    def add(self,data):
        new_node=Node(data) #Object of the Node class
        if self.__head is None:
            self.__head=self.__tail=new_node #here head and tail becomes the object of the node class and now they 
                                             #too have all properties as that of a Node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
    def display(self):
        temp=self.__head
        while temp is not None:
            print(temp.get_data(),end=" ")
            temp=temp.get_next()
        print("")

    def find_node(self,data):
        temp=self.__head
        while temp is not None:
            if temp.get_data()==data:
                return temp
            else:
                temp=temp.get_next()
        return None
    def insert(self,data,data_before):
        new_node=Node(data)
        if data_before==None:
            new_node.set_next(self.__head)
            self.__head=new_node
            if new_node.get_next()==None:
                self.__tail=new_node
        else:
            find_node=self.find_node(data_before)
            if find_node is not None:
                new_node.set_next(find_node.get_next())
                find_node.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail=new_node

    def delete(self,data):
        node_to_delete=self.find_node(data)
        if node_to_delete is not None:
            if node_to_delete==self.__head:
                self.__head=node_to_delete.get_next()
                if node_to_delete==self.__tail:
                    self.__tail=None
            else:
                print("inside else")
                temp=self.__head
                while temp is not None:
                    if temp.get_next()==node_to_delete:
                        temp.set_next(node_to_delete.get_next())
                        if node_to_delete==self.__tail:
                            self.__tail=temp
                        break
                    temp=temp.get_next()
        else:
            print("Node not found")

    def __str__(self):
        temp=self.__head
        m=[]
        while temp is not None:
            m.append(str(temp.get_data()))
            temp=temp.get_next()
        msg="--->".join(m)
        return "linked list created is : "+msg
        
#here we have created two extra methods in class LINkedList i.e set_head() and
#set_tail() for setting head and tail.
#if we create reverse() method inside list then there is no need of these two methods
#but they are needed if we are creating reverse() method outside list
def reverse_list(link_list):
    head = link_list.get_head()
    temp= link_list.get_head().get_next()
    while head != link_list.get_tail():
        temp_next=temp.get_next()
        temp.set_next(head)
        head= temp
        temp=temp_next
    link_list.get_head().set_next(None)
    a=link_list.get_head()
    b=link_list.get_tail()
    link_list.set_head(b)
    link_list.set_tail(a)
list1=LinkedList()
list1.add(15)
list1.add(16)
list1.add(18)
list1.add(186)
list1.add(58)
list1.add(189)
print("Original list=>",list1.__str__())
reverse_list(list1)
print("Reversed list=>",list1.__str__())
