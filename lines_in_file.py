file = open("coding.txt", 'r')

counter = 0

content = file.read()

contentNo = content.split('\n')

for i in contentNo:
    if i:
        counter = counter + 1

print("The number of lines is ", counter)