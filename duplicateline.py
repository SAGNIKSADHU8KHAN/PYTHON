outputfile = open("new_file.txt", 'w')

inputfile = open("hello.txt", 'r')

line_seen_so_far = set()

for line in inputfile:
    if line not in line_seen_so_far:
        
        line_seen_so_far.add(line)
        outputfile.write(line)

      

inputfile.close()
outputfile.close()