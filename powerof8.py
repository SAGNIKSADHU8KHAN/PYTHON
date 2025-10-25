num = int(input("Enter a number "))

if num <= 0:
    print("No, it's not the power of 8 .")

elif(num &(num -1))!= 0:
    print("No, it's not the power of 8")

else:
    n = num 
    count = 0
    while n > 1:
        n >>= 1
        count += 1

    if count%3 == 0:
        k = count // 3

        print("Yes,{num} is the power of 8")
        print(f"{num} = 8^{k}")

    else:

        print("No, {num} is not the power of 8")

