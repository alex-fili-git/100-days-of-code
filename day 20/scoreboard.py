from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highScore.txt") as file:
            self.highScore = int(file.read())
        self.draw()

    def draw(self):
        self.pu()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.write(f"Score = {self.score} High Score = {self.highScore}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.draw()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("highScore.txt", mode="w") as file:
                file.write(f"{self.highScore}")

        self.score = -1
        self.update()
