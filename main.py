import turtle

def staircase(size, nb):
    for i in range(0, nb):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)


t = turtle.Turtle()
staircase(50, 5)
t.forward(38)
turtle.done()
