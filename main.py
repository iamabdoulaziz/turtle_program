import turtle

def square(size):
    for i in range(0, 4):
        t.left(90)
        t.forward(size)


def squares(init_size, nb):
    for i in range(0, nb):
        size = (i + 1) * nb
        square(size)


t = turtle.Turtle()
squares(500, 15)
turtle.done()
