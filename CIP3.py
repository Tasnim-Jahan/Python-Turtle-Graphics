import turtle


def square():
    turtle.color("red")
    turtle.pendown()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.penup()


def circle():
    turtle.color("orange")
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()


def triangle():
    turtle.color("green")
    turtle.pendown()
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.penup()


def main():
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-200, 0)

    square()
    turtle.forward(150)

    circle()
    turtle.forward(150)

    triangle()

    turtle.done()


main()
