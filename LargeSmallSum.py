def LargeSmallSum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) <=3:
        return 0
    
    even_index_array = []
    odd_index_array= []
    
    for i in range(len(arr)):
        if i%2 == 0:
            even_index_array.append(arr[i])
            
        elif i%2 != 0:
            odd_index_array.append(arr[i])
            
    even_index_array.sort()
    odd_index_array.sort()
    
    return even_index_array[-2] + odd_index_array[-2]
        
list = [3,2,1,7,5,4]   
print(LargeSmallSum(list))    
