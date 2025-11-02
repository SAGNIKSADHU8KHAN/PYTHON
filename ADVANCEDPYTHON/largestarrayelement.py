def Maxelementarray(a):

    length = len(a)

    if length == 1:
        return a[0]
    
    return max(a[0], Maxelementarray(a[1:]))

array =[ 23, 56, 79, 96, 45]

print("The largest number in the array", Maxelementarray(array))