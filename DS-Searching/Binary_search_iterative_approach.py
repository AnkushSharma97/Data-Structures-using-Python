#Using iterative approach

def binary_search(n,item_list,low,high):
    comp=0
    while low <= high:
        comp+=1
        mid=(low+high)//2
        if n==item_list[mid]:
            x= 'item found at index '+str(mid)+'\n'+'and total comparisons made is '+str(comp)
            return x
        elif n > item_list[mid]:
            low=mid+1
        else:
            high=mid-1
    return 'element not found'

item_list=[1,4,6,9,12,45]
low=0
high=len(item_list)-1
print(binary_search(12,item_list,low,high))

#recurrence relation for above code= T(n) = T(n/2) +c
#time complexity = O(log n)
#space complexity=(1) (using recursive it is O(log n))
#therefore iterative aproach is more efficient in
#terms of space complexity.
            
        
