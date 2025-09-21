largest_number = int(input("Enter the largest number :"))

smallest_number = int(input("Enter the smallest number :"))

while(smallest_number):

    number_to_store = smallest_number
    smallest_number = largest_number % smallest_number

    largest_number = number_to_store

print(f"The HCF is {largest_number}")