from turtle import Turtle, Screen
import random

#tim = Turtle()
race_started = False
s = Screen()
s.listen()
s.setup(width=500, height=400)
user_bet = s.textinput(title="Make your bet.", prompt="Which turtle do you think will win?")
y_positions = [-75, -45, -15, 15, 45, 75]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_started = True

while race_started:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_started = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You Win!")
            else:
                print(f"You lose, the winner was {winning_color}")
        turtle.forward(random.randint(0,10))
    





s.exitonclick()
