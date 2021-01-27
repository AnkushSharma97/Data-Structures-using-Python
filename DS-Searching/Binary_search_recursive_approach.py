#Using recursive approach
comp=0
def binary_search(n,item_list,low,high):
    global comp #to get number of comparisons
    comp+=1
    mid=(low+high)//2
    if low <= high:
        
        if n==item_list[mid]:
            x= 'item found at index '+str(mid)+'\n'+'and total comparisons made is '+str(comp)
            return x
        elif n > item_list[mid]:
            low=mid+1
            return binary_search(n,item_list,low,high)
        else:
            high=mid-1
            return binary_search(n,item_list,low,high)
    return 'element not found'

item_list=[1,4,6,9,12,45]
low=0
high=len(item_list)-1
print(binary_search(4,item_list,low,high))

#recurrence relation for above code= T(n) = T(n/2) +c
#time complexity = O(log n)
#space complexity=(O(log n) (using iterative it is O(1))
#therefore iterative aproach is more efficient in
#terms of space complexity.

            
        
