def myfunction(n):

    print("Calculating the complexities ...\n")

    for i in range(0, n+1):
        print("First loop-")

    print("-> The time complexity of first loop : O(n)\n")

    j =1 
    while j <= n +1:
        print("Second loop",j)
        j = j * 2
    print("-> The time complexity of second loop : O(log n )\n ")

    for i in range(0, 100):
        print("Third loop -")

    print("The time complexity of third loop : O(1)\n ")

    print("Total time complexity ; O(n)")


n = int(input("Enter a number "))

myfunction(n)