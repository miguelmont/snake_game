from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Verdana", 15, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.open_file()
        self.hideturtle()
        self.goto(0,270)
        self.color("green")
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Verdana", 15, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if  self.score > int(self.highscore):
            self.highscore = self.score
            self.write_file(self.highscore)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
    
    def open_file(self):
        with open("data.txt") as f:
            return f.read(1)

    def write_file(self, new_highscore):
        with open("data.txt", "w") as f:
            f.write(str(new_highscore))