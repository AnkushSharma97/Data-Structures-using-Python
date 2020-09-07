#way 1 :--> Not preferred for interview ...(simplest one)
a=[10,20,25,27]
b=[12,14,16,23,45,67]
def mergesorted(a,b):
   merged_array=a+b
   merged_array.sort()
   return(merged_array)
print(mergesorted(a,b))
    

#way 2 :--> Using nested loops (Good for initial discussion in interview , but not a preferred way due to high complexity

#way 3 :--> Logical and most suited way for interview
def mergesorted(a,b):
    merged_array=[]
    i=0  #starting array for array a
    j=0  #starting index for array b
    iteration=0 #for checking complexity

    while i<len(a) and j<len(b):
        iteration+=1
        if a[i]<b[j]:
            merged_array.append(a[i])
            i+=1
        else:
            merged_array.append(b[j])
            j+=1
    print('Total iteratons',iteration) #this is just to get complexity
    #this loop will iterate only till length of smallest array times for both arrays.
    merged_array+=a[i:]+b[j:] # to append the remaining part of largest array
    return(merged_array)

array1=[10,20,25,27]
array2=[12,15,18,24,40]

print('merged array=',mergesorted(array1,array2))

#n= no. of items in array a
#m= no. of items in array b
# therefore, complexity till line 28 = O(n+m)
#k= remaining items iteration from largest array i.e. line 30
# therefore overall complecity = O(n+m+k)










