import turtle

turtle.Screen().bgcolor("red")

sc = turtle.Screen()

sc.setup (400,300)

turtle.title("Welcome to Turtle window ")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)

    i = i +1

turtle.done()