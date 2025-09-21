binary = input("Enter a number :")

binary = binary[::-1]

decimal = 0 

for i in range(len(binary)):
    if binary[i] == "1":
        decimal += 2 ** i 

print("The decimal value is",decimal)