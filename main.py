from turtle import Screen, Turtle
import tkinter as TK
import time
from snake import Snake
from food import Food
from score import Score

game_is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
#screen.onkey(lambda: game_is_on=False, "q")



while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_point()
        snake.extend()
    if snake.head.xcor() in (-280, 280) or snake.head.ycor() in (-280, 280):
        score.game_over()
    
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.game_over()


screen.exitonclick()