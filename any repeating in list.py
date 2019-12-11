__author__ = 'huzef'
def anyRepeating( arr, n):
    ''' First check all the values that are
     present in an array then go to that
     values as indexes and increment by
     the size of array'''
    for i in range(n):
        index = arr[i] % n
        arr[index] += n

    ''' Now check which value exists more
     than once by dividing with the size
     of array'''
    for i in range(n):
        if (arr[i]/n) > 1:
            return True
    return False

print anyRepeating([1,2,3,4],4)