def printPaths(path, r, c):
  
    if r == 1 and c == 1:
        print(path)
        return

    if r > 1:
        printPaths(path + "D", r - 1, c)

    if c > 1:
        printPaths(path + "R", r, c - 1)


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("All possible ways:")
printPaths("", rows, cols)