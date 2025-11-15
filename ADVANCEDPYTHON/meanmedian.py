def Mean(arr, arr_size):

    total_sum = 0
    for i in range(0, arr_size):
        total_sum += arr[i]

    return float(total_sum/arr_size)

def Median(arr, arr_size):

    sorted(arr)
    if arr_size % 2!= 0:
        return float (arr[int(arr_size/2)])
    
    return float ((arr[int(arr_size-1/2)])+arr[int(arr_size/2)]/2.0)

array = [23, 5, 6, 12, 72, 5, 9]
arr_size = len(array)

print("Mean", Mean(array, arr_size))
print("Median", Median(array, arr_size))