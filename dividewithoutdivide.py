def divide(ourdividend, ourdivisor):

    sign = (-1 if((ourdividend > 0) ^ (ourdivisor > 0))else 1)

    ourdividend = abs(ourdividend)
    ourdivisor = abs(ourdivisor)

    quotientnumber = 0
    tempnumber = 0

    for i in range(31, -1, -1):

        if(tempnumber +( ourdivisor << i ) <= ourdividend):
            tempnumber += ourdivisor << i
            quotientnumber |= 1 << i

    if sign == -1:
        quotientnumber = -quotientnumber
    return quotientnumber 

a = int(input("Enter a for a/b :"))
b = int(input("Enter b for a/b :"))
print("Result of",a, "/",b, "is",divide(a,b))