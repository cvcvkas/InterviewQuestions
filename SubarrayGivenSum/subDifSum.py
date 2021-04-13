def subArraySum(arr, s): 
    for x in range(len(arr)+1):
        for y in range(len(arr)+1):
            if (x < y):
                if (sum(arr[x:y]) == s):
                    return arr[x:y]
    return None
            
            
print(subArraySum([1,2,3,4,5,6,7,8,9,10], 55))
print(subArraySum([1,2,3,4,5,6,7,8,9,10], 30))