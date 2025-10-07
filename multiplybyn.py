def multiply_one_iteration(a, b):
    return a * b

def multiply_n_iterations(a, b):
    result = 0
    for i in range(abs(b)):
        result += 0
    if b < 0:
        result = - result

    return result

a = int(input("Enter a number "))
b = int(input("Enter another number "))

print("\n Using one iteration method", multiply_one_iteration(a, b))
print("\n Using N iterawtion method", multiply_n_iterations(a, b))