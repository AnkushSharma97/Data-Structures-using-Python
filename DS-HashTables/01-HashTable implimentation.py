
class HashTable:

    def __init__(self,size):
        self.__data = [None]*size

    #hash function for getting address. Complexity=O(1) because it just iterates over
    #complete key not all values hence very fast   
    def hash(self,key):
            hash=0
            for i in range(len(key)):
                hash=(hash+ ord(key[i])*i)
            return hash % len(self.__data)
        
    #method for inserting values to hash table
    def set(self,key,value):
        self.address=self.hash(key)  # pass the key to hash function for getting memory address
        if self.__data[self.address]==None: #if there is nothing at that address means no collision then:-
            self.__data[self.address]=[]    #create bucket, here we have created bucket of type list. 
        self.__data[self.address].append([key,value])#add (key,value) pairs to that bucket
        print(self.__data)
        #print(self.__data)
        #Complexity = depends upon collisions and type of bucket
        #For e.g.:- here we are using Linked List as Bucket and inserting values at end then Complexity =O(n) because
        #inserting values at end of Linked list includes traversing complete list unlike arrays (const time) and hence Comp =O(n)
    
    #method for accessing values with help of keys
    def get(self,key):
        self.address=self.hash(key) #getting memory address where we have to look fo value
        demo=self.__data[self.address]
        if demo==None:  #if key is not present 
            return None
        else:           #accessing values if key is present
            for i in range(len(demo)):
                        if demo[i][0]==key:
                           print(demo[i][1])
    def keys(self):
        keys=[]
        for i in self.__data:
            if i != None:
                if len(i)>1:
                    for j in i:
                        keys.append(j[0])
                else:
                    keys.append(i[0][0])
        return keys
        
    #complexity :- depends upon collision (and it depends upon hash function) but most of the times it is < O(n) snd in worst case we can consider it as O(n)

a=HashTable(10)
a.set('grapes',1000)
#a.set('grapes',60) this is anomaly in our code that if we add one updated key value pair then it is storin it as
#new value i.e. there will be two keys with same name which is not acceptable
a.set('grapess',10040)
a.set('oranges',100)
a.get('grapes')
print(a.keys())

#the hash function we have written is just for example purpose ..because
#00) It is accepting only strings but in actual key can be of any data type.
#01) Also if we are giving ('grapes',1000) two times , then it will make two entries for it i.e. two same keys
#    but in actual key is unique i.e. only one can be there with same name.

