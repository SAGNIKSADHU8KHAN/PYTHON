file_read = open("coding.txt", 'r')

print(file_read.read())

file_read.close()

file_write = open("coding.txt", 'w')

file_write.write("I love travelling a lot, and exploring new places.")
file_write.write("I love visiting the old houses in Kolkata.")

file_write.close()

file_append = open("coding.txt", 'a')

file_append.write("\n I also love exploring mountains. The last time i had a tour of mountains was at Dehradun, Uttarakhand.")

file_append.close()