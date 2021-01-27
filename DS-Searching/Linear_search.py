def linear_search(n,list_of_items):
    comparisons=0
    for i in list_of_items:
        comparisons+=1
        if i==n:
            print('Total comarisons:',comparisons)
            return 'element found'
    return 'element not found'
print(linear_search(12,[9,4,34,1,6,12,45]))
