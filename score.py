from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Verdana", 15, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0,270)
        self.color("green")
        self.write("Score: 0", align="center", font=("Verdana", 15, "bold"))

    def score_point(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)