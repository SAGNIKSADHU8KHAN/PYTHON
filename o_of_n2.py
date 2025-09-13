def ONSquareTime(n):
    iteration = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("*")
            iteration+=1

        print("  ")
    print("\n When n is", n, "\n then iteration is", iteration)

ONSquareTime(10)
ONSquareTime(20)