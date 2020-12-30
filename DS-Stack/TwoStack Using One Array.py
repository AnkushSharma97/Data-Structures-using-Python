#___________________Implementing two stacks using One Array.___________________
'''Problem:-
Usually when we are trying to implement a Stack using Array we use a single
Array to implement a single Stack. But here we need to implement two stacks
using a single Array only.

#Below Question copied from GeeksforGeeks....

The task is to create a data structure twoStacks that represents two stacks.
Implementation of twoStacks should use only one array, i.e., both stacks
should use the same array for storing elements. Following functions must be
supported by twoStacks.
push1(int x) --> pushes x to first stack.
push2(int x) --> pushes x to second stack.
pop1() --> pops an element from the first stack and return the popped element.
pop2() --> pops an element from the second stack and return the popped element.

Note: Implementation of twoStack should be space efficient.


Method 1 (Divide the space in two halves): A simple way to implement two stacks
is to divide the array into two halves and assign the half space to the first
stack and the other half to the second stack, i.e., use arr[0] to arr[n/2] for
stack1, and arr[(n/2) + 1] to arr[n-1] for stack2 where arr[] is the array to
be used to implement two stacks and size of array be n.

The problem with this method is an inefficient use of array space. A stack push
operation may result in stack overflow even if there is space available in arr[].
For example, say the array size is 6 and we push 3 elements to stack1 and do not
push anything to the second stack2. When we push the 4th element to stack1, there
will be overflow even if we have space for 3 more elements in the array.

Method 2 (A space-efficient implementation): This method efficiently utilizes the
available space. It doesn't cause an overflow if there is space available in arr[].
The idea is to start two stacks from two extreme corners of arr[]. The first
stack, stack1 starts from the leftmost element, the first element in stack1 is
pushed at index 0. The second stack, stack2 starts from the rightmost corner, the
first element in stack2 is pushed at index (n-1). Both stacks grow (or shrink) in
opposite direction. To check for overflow, all we need to check is for space
between top elements of both stacks.'''

#We will follow the second approach(method 2) to implement our code.

class TwoStack:
    def __init__(self,maxsize):
        self.__max_size=maxsize
        self.__elements=[None]*maxsize
        self.__top1=-1
        self.__top2=maxsize

    def push1(self,data):
        if self.__top1+1<self.__top2:
            self.__top1+=1
            self.__elements[self.__top1]=data
        else:
            print("Stack overflow")

    def push2(self,data):
        if self.__top1+1<self.__top2 :  #or self.__Top2 > self.__top1+1:
            self.__top2-=1
            self.__elements[self.__top2]=data
        else:
            print("Stack overflow")


    def pop1(self):
        if self.__top1==-1:
            print("Stackk empty,underflow condition")
        else:
            item=self.__elements[self.__top1]
            self.__top1-=1
            print("item deleted is",item)

    def pop2(self):
        if self.__top2==self.__max_size:
            print("Stack empy,underflow")
        else:
            item=self.__elements[self.__top2]
            self.__top2+=1
            print("item deleted from 2nd stack is",item)

    def __str__(self):
        x=self.__elements[0:self.__top1+1]
        y=self.__elements[self.__top2:]
        print("elements in first stack",x)
        print("elements in second stack",y)
        print("complete stack1 + stack2",end=" ")
        return str(x+y)
stack=TwoStack(5)
stack.push1(3)
stack.push1(40)
stack.push1(39)
stack.push2(56)
stack.push2(67)

print(stack)



