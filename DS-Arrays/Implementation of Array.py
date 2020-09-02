'''This implementation is just for understanding purpose because of various reasons:-
    1) We implement our own data structure only if the data structure is not internally implemented (or present inbuilt)
       using that language.
    2) Array data structure is already implemented internally in python and we can use that by importing Array module.
    3) The main property of array is that it contains homogeneous type of elements only but in the implementaion done below
       it can hold all type of data at one time in a single array.
    So this impementation is just for understanding purpose and nothing else.'''

class MyArray:
    def __init__(self):
        self.length=0
        self.data={}

    def __str__(self):
            return(str(self.__dict__))
        
    def get(self,index):
            return(self.data[index])
        
    def push(self,item):
            self.data[self.length]=item
            self.length+=1
            
    def pop(self):
            lastitem=self.data[self.length-1]
            self.data.pop(self.length-1)
            self.length-=1
            return lastitem
        
    def delete(self,index):
            deleteditem=self.data[index]
            for i in range(index,len(self.data)-1):
                self.data[i]=self.data[i+1]
            self.pop()
            return deleteditem
        
    def insert (self,index,value):
        if index >= len(self.data):
            self.push(value)
        else:
            for i in range(self.length,index,-1):
                self.data[i]=self.data[i-1]
            self.data[index]=value
            self.length+=1

arr=MyArray()
arr.push(50)
arr.push(60)
arr.push(80)
arr.push(87)
#arr.delete(1)
arr.insert(1,80)
print(arr)
