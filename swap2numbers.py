def swap1(a, b):

    print("Before swapping: a =", a, "b =",b)

    a = a ^ b
    b = a ^ b
    a = a ^ b

    print("After swapping: a = ",a, "b=",b)

def swap2(a, b):

    print("Before swapping: a =",a, "b =",b)

    a = (a & b) + (a | b)
    b = a + ~b + 1
    a = a +~b +1

    print("After swapping: a =",a, "b =",b )

swap1(10,12)
swap2(30,40)


