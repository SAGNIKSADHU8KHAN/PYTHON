def minelement(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = min(temp, a[i])
    return temp

def maxelement(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = max(temp, a[i])
    return temp

a = [23, 42, 17, 88, 34]
size = len(a)
print("Minimum number = ", minelement(a,size))
print("Maximum number =", maxelement(a, size))
