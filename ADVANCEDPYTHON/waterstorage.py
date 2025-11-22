def water(a, a_size):

    left_tallest = [0]*a_size

    right_tallest = [0]*a_size

    water = 0

    left_tallest[0] = a[0]
    for i in range(1, a_size):
        left_tallest[i] = max(left_tallest[i-1],a[i])

    right_tallest[a_size -1] = a[a_size-1]
    for i in range(a_size -2, -1, -1):
        
