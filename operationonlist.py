lst = [ "apple", "banana", "kiwi", "mango", "guava"]

print("Length of list ", len(lst))
print("First element", lst[0])
print("Last element", lst[-1])

lst.append("papaya")

print("Append list", lst)

lst.remove("guava")

print("Removed list", lst)

lst.sort()
print("sorted list", lst)

lst.pop(3)
print("poped list", lst)

lst.reverse()
print("Reversed list", lst)

print("multiplication of list", lst * 2)

lst[:3]
print("sliced list", lst)

lst.clear()
print(lst)
      