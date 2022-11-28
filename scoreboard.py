from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto", 18, "normal")

# read highscore from file. using with open to close file automatically
with open("highscore.txt") as file:
    highscore = int(file.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = highscore
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.write(f"GAME OVER - Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
