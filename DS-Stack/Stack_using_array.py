class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top==self.__max_size-1:
            return True
        return False

    def push(self,data):
        if self.is_full():
            print("Stack overflow, no place for",data)
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def is_empty(self):
        if self.__top==-1:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            return("stack underflow nothing to pop")
        else:
            temp=self.__elements[self.__top]
            self.__elements[self.__top]=None
            self.__top-=1
            return temp
    def display(self):
        index=self.__top
        while index>=0:
            print(self.__elements[index])
            index-=1

    def __str__(self):
        index=self.__top
        print("stack elements from top to bottom")
        for i in range(index,-1,-1):
            if i==index:
                print(str(self.__elements[i]),'-----> Top')
            elif i==0:
                print(str(self.__elements[i]),'-----> Bottom')
            else:
                print(str(self.__elements[i]))
        

stack=Stack(5)
stack2=Stack(5)
print(stack2.pop())
stack.push('Ankush')
stack.push('rahul')
stack.push('modi')
stack.push('Amit')
stack.push('Jai Ram')
print("element popped is",stack.pop())
stack.push('Bihari')
stack.display()
