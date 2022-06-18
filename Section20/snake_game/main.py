from turtle import Screen, Turtle
import turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey snake!")
screen.tracer(0)

snake = Snake()


game_on = True
while game_on:
    screen.update()
    time.sleep(snake.snake_speed)
    
    snake.move()



screen.exitonclick()