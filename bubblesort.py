def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =arr[j+1] , arr[j]
    return arr

def recursive_bubbleSort(arr, n):
    if n==1:
        return
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] =arr[j+1] , arr[j]
    recursive_bubbleSort(arr, n-1)
    return arr

arr = [5,4,3,2,1]
print(bubbleSort(arr))
print(recursive_bubbleSort(arr, len(arr)))