def max_difference(arr):

    min_element = arr[0]
    max_dif = arr[1]-arr[0]

    for i in range(1, len(arr)):

        max_dif = max(max_dif, arr[i]- min_element)

        min_element = min(min_element, arr[i])
    
    return max_dif

a = [4, 5, 234, 2, 6, 82, 234, 5234]

print("Maximum difference", max_difference(a))