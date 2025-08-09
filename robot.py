class Robot:
    def __init__(self, name):
        self.name = name  
    
    def introduce(self):
        print(f"Hello, I am {self.name}!")

# Creating two robot objects
robot1 = Robot("Tom")
robot2 = Robot("Jerry")

# Making them introduce themselves
robot1.introduce()
robot2.introduce()