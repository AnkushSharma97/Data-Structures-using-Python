'''Reversing a string:- We can reverse a string in python or in any coding language in many ways. We will use following two ways here:-
    1) Writing our own logic
    2) String reversal using slicing
    3) Converting string to list and then reverse it and again join it
    4) Converting string to list and then popping last element and saving it to new string
String :- String is just an array or more specifically an array of characters. This means that String also supports both +ve and -ve indexing
          and we can iterate through it. We will use this concept in our problem'''

'''1) Writing our own logic:- Just start from the last character and loop till the first one.'''
def rev(string):
    revstring=''
    for i in range(len(string)-1,-1,-1):
        revstring+=string[i]
    return revstring

print(rev("I am groot"))

'''2) Using Slicing:- Here also we will start from last character till first one'''
def reverse(string):
    return string[::-1] #Syntax:- string[start:end:increment] and this return stmt can also be written as: string[-1:-(len(string)+1):-1]
print(reverse("Hi This is Ankush"))
    
'''3) Converting string to list and then reverse it and again join it'''
def reverse2(string):
    tolist=list(string)#string to list
    tolist.reverse()#reversing the string
    string=('').join(tolist)#list to string again
    return string
print(reverse2("I am groot"))

'''4) Converting string to list and then popping last element and saving it to new string '''
def reverse3(string):
    tolist=list(string)
    string=''
    for i in range(len(tolist)):
        string+=tolist.pop()
    return(string)
print(reverse3("I am groot"))
