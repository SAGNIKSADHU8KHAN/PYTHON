with open("coding.txt", 'w') as file:
    file.write("Hi this is penguin and i'm one year old. \n I also love travelling a lot")

file.close()

with open("coding.txt", 'r') as file:

    data = file.readlines()

    for line in data:
        word = line.split()
        print(word)

file.close()
          