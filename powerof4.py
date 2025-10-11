def power0f4(number):

    count = 0

    if (number & (~(number &(number- 1)))):

        while(number > 1):
            number >>= 1
            count+= 1

        if count % 2 == 0:
            return True
        else:
            return False
        
number = int(input("Enter a number :"))

if power0f4(number):
    print(f" The {number} is power of 4 ")

else:
    print(f"The {number} is not power of 4")
