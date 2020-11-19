class Node:
    def __init__(self,data):
        self.__data=data
        self.__previous=None
        self.__next=None

    def get_data(self):
        return self.__data
    def set_data(self,data):
        self.__data=data
    def get_previous(self):
        return self.__previous
    def set_previous(self,previous):
        self.__previous=previous
    def get_next(self):
        return self.__next
    def set_next(self,next):
        self.__next=next

class Dlinklist:
    def __init__(self):
        self.__head=None
        self.__tail=None
    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail
    def add(self,data):
        newNode=Node(data)
        if self.__head==None and self.__tail==None:
            self.__head=self.__tail=newNode
        else:
            self.__tail.set_next(newNode)
            newNode.set_previous(self.__tail)
            self.__tail=newNode
    def find_node(self,data):
        temp=self.__head
        while temp is not None:
            if temp.get_data()== data:
                print("node found")
                return temp
            temp=temp.get_next()
        print("node not found")

    '''Insertion in a Doubly Linked list:-
        we can perform insertion operation in a oubly linked list in four ways:-
        1)At the front of DLL(prepend)
        2)After a given node
        3)At the end of DLL(add/append)
        4)Before a given node'''
    #1) Inserting Node after a given node i.e. when node_before/data_before
    #   is given.
    def insert(self,data,data_before):
        nodetoinsert=Node(data)
        temp=self.__head
        flag=0 #to know if data before is present in linked list or not
        if temp==None:  
            self.__head=self.__tail=nodetoinsert
        elif data_before==None:
            nodetoinsert.set_next(self.__head)
            self.__head.set_previous(nodetoinsert)
            self.__head=nodetoinsert
        while temp is not None:
            if temp.get_data()==data_before:
                flag=1
                nodetoinsert.set_next(temp.get_next())
                nodetoinsert.set_previous(temp)

                if temp.get_next() is not None:
                    temp.get_next().set_previous(nodetoinsert)
                    
                else:
                    self.__tail=nodetoinsert
                temp.set_next(nodetoinsert)
                break
            temp=temp.get_next()
        if flag==0:
            print("there is no node with data before",data_before)
    #2 Inserting a Node before a given Node i.e when node_after/data_after
    #is given
    def insert_before(self,data,data_after):
        find_node=self.find_node(data_after)
        newnode=Node(data)
        if self.__head==None:
            self.__head=self.__tail=newnode
        if data_after==None:
            self.__tail.set_next(newnode)
            newnode.set_previous(self.__tail)
            self.__tail=newnode
        elif find_node is not None:
            newnode.set_next(find_node)
            if find_node != self.__head: #or find_node.get_previous() is not None
                find_node.get_previous().set_next(newnode)
                newnode.set_previous(find_node.get_previous())
            else:
                self.__head=newnode
            find_node.set_previous(newnode)
        else:
            print("Node not found")
    def delete(self,data):
        find_node=self.find_node(data)
        if find_node==self.__head:
            self.__head=find_node.get_next()
            self.__head.set_previous(None)
        elif find_node is not None:
            find_node.get_previous().set_next(find_node.get_next())
            if find_node.get_next() is not None:
                find_node.get_next().set_previous(find_node.get_previous())
            else:
                self.__tail=find_node.get_previous()
            find_node.set_previous(None)
            find_node.set_next(None)
        else:
            print("There is no node with data",data)
    def display_from_end(self):
        temp=self.__tail
        while temp is not None:
            print(temp.get_data())
            temp=temp.get_previous()
            
dlist=Dlinklist()
dlist.add(90)
dlist.add(100)
dlist.add(120)
dlist.add(361)
#dlist.find_node(90)
#dlist.insert(110,100)
dlist.insert_before(110,None)
#dlist.delete(128)
dlist.display_from_end()
