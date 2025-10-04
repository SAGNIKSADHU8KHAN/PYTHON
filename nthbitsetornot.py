def SetorNot(number, n):

    if number & (1<<(n-1)):
        print("\n Set")

    else:
        print("\n Notset")

number = int(input("Enter a number :"))
bit = int(input("Enter a bit"))

SetorNot(number, bit)

