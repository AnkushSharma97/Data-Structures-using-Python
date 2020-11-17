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
        
    
list1=LinkedList()
list1.add(15)
list1.add(16)
list1.add(18)

print(list1.__str__())
list1.display()
''' demonstrate find node
x=list1.find_node(30)
if x is not None:
    print("Node found",x.get_data())
else:
    print("Node not found")
'''
list1.insert(56,30)
list1.delete(18)
print("head is=> ",list1.get_head().get_data())
print("tail is=> ",list1.get_tail().get_data())
print(list1.__str__())
                
'''
    def delete(self,data):
        temp=self.__head
        if temp.get_data()==data:
            self.__head=temp.get_next()
            if temp.get_next()==None:
                self.__tail=None
        else:
            
            while temp.get_next() is not None:
                if temp.get_next().get_data() == data:
                    temp.set_next(temp.get_next().get_next())
                    if temp.get_next() is None:
                        self.__tail=temp
                    break
                else:
                    temp = temp.get_next()
''' 
    
            
        





