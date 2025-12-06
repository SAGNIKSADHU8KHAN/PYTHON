def subarraysum(array, n, sum):

    for i in range(n):
        curr_sum = array[i]

        j = i+1
        while j <= n:

            if curr_sum == sum:
                print("Sum found between")
                print("Indexes %d and %d"%(i, j-1))

                return 1
            
            if curr_sum > sum or j == n:
                break

            curr_sum = curr_sum +array[j]

            j+=1


    print("No subarray found")
    return 0


array = [3, 6, 2, 2, 56, 1, 0, 9]
n = len(array)
sum = 10
subarraysum(array, n, sum)


