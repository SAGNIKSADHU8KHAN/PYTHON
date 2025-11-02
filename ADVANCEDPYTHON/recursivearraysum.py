def arraytotalsum(a):

    length = len(a)

    if length == 1:

        return a[0]
    
    return a[0] +arraytotalsum(a[1:])

array = [1, 3, 4, 7, 9]

print("The total sum of the array elements", arraytotalsum(array))