# Lecture notes/code snips from lecture/etc

# Turtle Event Listeners
from turtle import Turtle, Screen

tim = Turtle()
s = Screen()

def move_forward():
    tim.forward(10)

s.listen()
s.onkey(key="space", fun=move_forward)
s.exitonclick()

#passing a function to another function
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)

print(calculator(3, 5, add))