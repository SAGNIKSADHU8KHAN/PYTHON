number = int(input("Enter a number"))

original_number = number 

reversed_number = 0 

while number > 0:

    digit = number % 10

    reversed_number = reversed_number * 10 + digit 
    
    number = number // 10

if reversed_number == original_number:

    print(f"{original_number} is a Palindrome Number.")

else:

    print(f"{original_number} is not a Palindrome number .")
