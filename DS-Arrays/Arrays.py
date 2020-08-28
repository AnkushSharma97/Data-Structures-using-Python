#Arrays Introduction

#creating array in python
from array import array

arr=array('I',(40,53,26,57)) #syntax:- array('type code','grouped data')
#here type code='I' it is for integer and it takes 2 bytes space
#for each element i.e. 2 shelfs for each element
#Total storage = 4 items * 2 bytes for each item= 4*2=8 bytes

#Accessing any element
print('third element is',arr[2]) # O(1)

#push or inserting element at end
arr.append(72) # O(1)

print('array after insert operation at end',arr)

#inserting element at any random index
arr.insert(3,45) #inserting 45 at index 3 that is 4th position
#O(n) bcause we have to perfom shifting till end
print('array after inserting 45 at index 3 that is 4th position',arr)


#Deleting elements from array
'''three ways:-
1) Using pop function:-
        Syntax:- array.pop(index)  [index is optional]
                 if index is given
                     then it will delete from the specified index
                     Complexity=O(n)
                 else
                     Delete from from end
                     Complexity=O(1)
2)Using remove function:-
        Syntax:-array.remove(value)
                Removes the first occourence of specified value
                Complexity=O(n)
3) Using del operator:-
        Syntax:-1) del arrayname[index] #for deleting values at particular index
                   Complexity=O(n)
                   
                2) del arrayname         #for deleting complete array

'''
arr.pop()
print('Array after removing last element from above array',arr)

arr.pop(0)
print('Array after removing 1st value',arr)
                
arr.remove(45)
print('Removing 45 from array',arr)

del arr[1]
print('Removing 2nd value from array',arr)

del arr #complete array deleted
print ('we will get error if we try to print array because it has been deleted')
print(arr)
