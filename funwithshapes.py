import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue") 

pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)
pen.shape("turtle")

def draw_shape(points, fill_color):
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.fillcolor(fill_color)
    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0]) 
    pen.end_fill()

triangle_points = [(-200, 100), (-150, 186), (-100, 100)]
draw_shape(triangle_points, "pink")

rectangle_points = [(0, 100), (150, 100), (150, 20), (0, 20)]
draw_shape(rectangle_points, "lightgreen")

def draw_hexagon(center_x, center_y, size, fill_color):
    pen.penup()
    pen.goto(center_x, center_y)
    pen.forward(size)
    pen.left(90 + 30) 
    pen.pendown()
    pen.fillcolor(fill_color)
    pen.begin_fill()
    for _ in range(6):
        pen.forward(size)
        pen.left(60)
    pen.end_fill()
    pen.setheading(0)


draw_hexagon(-75, -100, 60, "yellow")

pen.hideturtle()
turtle.done()
