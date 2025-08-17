firstfile = input("Enter the name of the first file ")
secondfile = input("Enter the name of the second file")

f1 = open("Block1.txt", 'r')
f2 = open("Block2.txt", 'r')

print("Content of the first file before appending - \n", f1.read())
print("Content of the second file before appending -\n", f2.read())

f1.close()
f2.close()

f1 = open("Block1.txt", 'a')
f2 = open("Block2.txt", 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

# print("Content of the first file after appending - \n ", f1.read())
print("Content of the second file after appending - \n", f2.read())

f1.close()
f2.close()

