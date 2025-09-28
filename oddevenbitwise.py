def IsEvenOdd(n):

    if(n^1 == n+1):
        return True
    else:
        return False
    
number = int(input("Enter a number"))

if IsEvenOdd(number):
    print(number, " is a even number")
else:
    print(number, "is a odd number")
       