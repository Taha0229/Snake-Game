from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.goto(x=0, y=250)
        self.speed("fastest")
        self.hideturtle()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.update_scoreboard()

    def score_incrementer(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w', ) as file:
                file.write(str(self.highscore))


        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscore},", align='center', font=("Courier", 24, "normal"))