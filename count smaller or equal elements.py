def binarySearchCount(arr,key): 
    left = 0
    right = len(arr)
    mid=0
    while (left < right): 
        mid = (right + left)//2
        if (arr[mid] == key): 
            while (mid+1<n and arr[mid+1] == key): 
                 mid+=1
            break
        elif (arr[mid] > key): 
            right = mid 
        else: 
            left = mid + 1
    while (mid > -1 and  arr[mid] > key): 
        mid-=1
    return mid + 1