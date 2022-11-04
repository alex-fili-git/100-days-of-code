import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.pu()

states = pd.read_csv("50_states.csv")
states_list = states["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list and answer_state not in guessed_states:
        x_answer_state = int(states.loc[states["state"] == answer_state].x)
        y_answer_state = int(states.loc[states["state"] == answer_state].y)
        writer.goto(x=x_answer_state, y=y_answer_state)
        writer.write(answer_state)
        guessed_states.append(answer_state)

pd.DataFrame(list(set(states_list) - set(guessed_states))).to_csv("states_to_learn.csv")


turtle.mainloop()
