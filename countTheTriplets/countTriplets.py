def countTriplet(arr, verbose=False):
    count = 0
    
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x] + arr[y] in arr and y > x:
                if verbose: print(f"{arr[x]} + {arr[y]} = {arr[x] + arr[y]}")
                count += 1
                
    return count

print(countTriplet([1,2,3,4,5,6,7,8,9,10,11]))
print(countTriplet([5,4,3,6,9,7,8,1,5,78,9,1], True))