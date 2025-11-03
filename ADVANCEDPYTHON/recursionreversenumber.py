def reversenumber(num):

    if(num>0):

        last = num %10
        if(num%10 > 0):

            currentnumber = reversenumber((int)(num//10))

            return last *pow(10, len(str(currentnumber)))+ currentnumber
        
    return num
        
n = int(input("Enter an input "))
print("Reversed number", reversenumber(n))