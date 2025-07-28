my_set = {1, 1, 1, 2, 3, 4, 4, 4, 5, 5}
print("mY SET", my_set)

my_set.add(6)

print("Updated set", my_set)

set1 = my_set
set2 = {4, 5, 6, 7, 8, 9}

print("difference", set1.difference(set2))
print("symmetric difference", set1.symmetric_difference(set2))