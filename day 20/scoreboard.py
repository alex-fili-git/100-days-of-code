from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.draw()

    def draw(self):
        self.pu()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.reset()
        self.score += 1
        self.draw()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)