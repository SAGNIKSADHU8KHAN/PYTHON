n = int(input("Enter a number "))

def checkifpower(n):
    if(n<=0):
        return False
    if(n==1):
        return True
    if(n%4 == 0):
        return checkifpower(n/4)
    
    return False

if(checkifpower(n)):
    print("Power of 4 ")

else:
    print("Not power of 4")