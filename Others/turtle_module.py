import turtle
you = turtle.Turtle()
# you.forward(100)
# you.left(45)
# you.forward(100)
ts = you.getscreen()
you.shape('turtle')
you.color('yellow')
ts.bgcolor('black')


def move():
    you.forward(2)


ts.onkey(move, 'space')
ts.listen()
turtle.done()

