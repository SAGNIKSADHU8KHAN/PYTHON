my_tuple = ()
print(my_tuple)

my_tuple = ( 1, 2, 3)
print(my_tuple)

my_tuple = ("Hello", 1, 3.5)
print(my_tuple)

my_tuple = ([1, 2, 3], "mina", ["hello", "Hi", "Good morning"])
print(my_tuple)

my_tuple = (1, 3, 5, 13, 18, 19)
print(my_tuple[2])

my_tuple = ([1, 2, 3], "mina", ["hello", "Hi", "Good morning"])
print(my_tuple[0][2])



sliced_tuple = my_tuple[1:3]
print(sliced_tuple)

for number in (my_tuple):
    print("Hello", number)
