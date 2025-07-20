def armstrong(num):

    power = len(str(num))
    total = sum(int(digit) ** power for digit in str(num))
    return num == total

number = int(input("Enter an number : "))

if armstrong(number):
    print(f" {number} is an Armstrong number.")

else:
    print(f" {number}  is not an Armstrong number")


