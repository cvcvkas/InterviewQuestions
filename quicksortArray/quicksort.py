arr = [9, 2, 5, 6, 4, 3, 7, 10, 1, 12, 8, 11];

def quicksort(array):
    if len(array) > 1:
        pivot = array[0]
        less = []
        equal = []
        greater = []


        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)

    else:
        return array




print(quicksort(arr[::]))