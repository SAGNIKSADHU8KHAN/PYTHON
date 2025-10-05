num = int(input("Enter number :"))

if num == 0:
    print("No set bit found.")

else:
    position = 1
    while num > 0:
        if num & 1:
            print("Position of the first set bit", position)
            
            break 
        num = num >> 1 
        position += 1