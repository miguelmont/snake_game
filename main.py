from turtle import Screen, Turtle
import tkinter as TK
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")

snake = Snake()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()





screen.exitonclick()