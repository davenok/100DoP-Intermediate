from turtle import Turtle, Screen

tim = Turtle()
s = Screen()
s.listen()

# Keys - WASD for movement, C to clear screen

def fwd():
    tim.forward(10)

def back():
    tim.backward(10)

def left():
    tim.setheading(tim.heading() + 10)

def right():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

s.onkey(key="w", fun=fwd)
s.onkey(key="a", fun=left)
s.onkey(key="s", fun=back)
s.onkey(key="d", fun=right)
s.onkey(key="c", fun=clear)

s.exitonclick()
