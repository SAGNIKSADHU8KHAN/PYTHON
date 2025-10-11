def  power2(number):

    if number == 0:
        return 0
    
    if (number & ~ (number-1)) == number:

        return 1
    return 0

number = int(input("Enter a number :"))

if power2(number):
    print(f" the {number} is the power of two ")

else:
    print(f" the {number} is not power of two")