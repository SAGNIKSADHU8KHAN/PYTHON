def checksorted(a):

    length = len(a)

    if length == 1 or length == 0:

        return True
    
    return a[0] <= a[1] and checksorted(a[1:])


a = [ 1, 2, 3, 9, 5, 6, 7]

if checksorted(a):

    print("This is an sorted array.")

else:
    print("This is not an sorted array")