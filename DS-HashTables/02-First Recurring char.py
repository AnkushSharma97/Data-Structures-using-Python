def recurring(array):
    hashtable={}
    for i in range(len(array)):   
        if array[i] not in hashtable:
            hashtable[array[i]]=i
        else:
            return array[i]
print(recurring([2,2,1,1,2]))


#Time Complexity= O(1)
#Space complexity= O(n) because we have added an extra DS i.e. hash table and in worst case
#it will store the complete array so O(n)
    
