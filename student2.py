class student:

    grade = 10
    name = "penguin"

    def introduction(self):

        print("I am a student")

    def details(self):

        print("I read in class", self.grade)
        print("My name is", self.name)

std1 = student()
std1.details()
std1.introduction()