num = int(input("Enter a number"))

count = 0
max_count = 0

n = num
while n > 0:
    if n & 1:
        count += 1
        max_count = max(max_count, count)

    else:
        count = 0
    n = n >> 1

print("Binary Representation :", bin(num)[2:])
print("Longest consecutive 1's length", max_count)
