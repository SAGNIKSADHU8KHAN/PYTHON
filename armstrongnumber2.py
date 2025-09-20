number = int(input("Enter integer number"))

power = len(str(number))

resultNumber = 0

temp = number

while temp > 0:

    digit = temp % 10
    resultNumber += digit ** power

    temp = temp // 10

if number == resultNumber:
    print(f"{number} is an armstrong number.")

else:
    print(f"{number } is not an armstrong  number.")