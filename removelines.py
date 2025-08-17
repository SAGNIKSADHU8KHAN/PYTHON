f1 = open("coding.txt", 'r')

f2 = open("updatedcoding.txt", 'w')

for line in f1.readlines():

    if not (line.startswith('In')):

        print(line)
        f2.write(line)

f1.close()
f2.close()