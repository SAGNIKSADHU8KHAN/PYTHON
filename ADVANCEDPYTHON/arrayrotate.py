def rotations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)

def rotate(a, a_size):
    temp = a[0]
    for i in range(a, a_size-1):
        a[i]= a[i+1]
    a[a_size -1 ]= temp

def printarray(a, a_size):
    for i in range(a_size):
        print("%d"% a[i], end = " ")
    print("/n")
b = [23, 56, 43, 34, 51, 23, 89, 99, 76]

printarray(b, len(b))
rotations(b, 2, len(b))
printarray(b, len(b))