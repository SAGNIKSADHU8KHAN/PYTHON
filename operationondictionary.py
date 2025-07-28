# empty dictionary

my_dict = { }

# divtionary with integer keys

my_dict = {1: "apple", 2: "banana"}

my_dict = {"name" : "John", 1: [1,2,4] }

my_dict = {"name": "Jack" , "age" : 18}

print(my_dict ["name"])
print(my_dict.get ("age"))

my_dict["age"] = 27
print(my_dict)

my_dict["address"] = "Howrah"
print(my_dict)

my_dict.pop("age")
print(my_dict)

print("Address :", my_dict.get("address"))

my_dict.clear()
print(my_dict)

