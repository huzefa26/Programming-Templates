__author__ = 'huzef'


def add(arr, N, lo, hi, val):
    arr[lo] += val
    if hi != N - 1:
        arr[hi + 1] -= val


def updateArray(arr, N):
    for i in range(1, N):
        arr[i] += arr[i - 1]


def printArr(arr, N):
    updateArray(arr, N)
    for i in range(N):
        print arr[i],
        print

    N = 6
    arr = [0 for i in range(N)]

    add(arr, N, 0, 2, 100)
    add(arr, N, 1, 5, 100)
    add(arr, N, 2, 3, 100)

    printArr(arr, N)
