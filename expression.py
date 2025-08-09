class Expression:
    def __init__(self, num1, num2, num3):
       
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def add_numbers(self):
        
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {result}")


exp1 = Expression(5, 10, 15)
exp1.add_numbers()

exp2 = Expression(20, 30, 40)
exp2.add_numbers()