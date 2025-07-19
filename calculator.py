def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x % y

num1 = int(input("Enter a number :"))
num2 = int(input("Enter an another number :"))

print("sum" , add(num1,num2))
print("subtract" , subtract(num1,num2))
print("Product" , multiply(num1,num2))
print("divide" , divide(num1,num2))