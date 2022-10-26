from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 65, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player1 = 0
        self.score_player2 = 0
        self.draw()

    def draw(self):
        self.pu()
        self.hideturtle()
        self.goto(x=-50, y=220)
        self.color("white")
        self.write(f"{self.score_player1}", align=ALIGNMENT, font=FONT)
        self.goto(x=50, y=220)
        self.write(f"{self.score_player2}", align=ALIGNMENT, font=FONT)

    def update(self, player):
        self.reset()
        if player == 2:
            self.score_player1 += 1
        else:
            self.score_player2 += 1
        self.draw()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)