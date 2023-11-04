import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
turtle.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct_guesses = []
answer_state = (screen.textinput(title="Guess the State", prompt="Guess a state's name")).title()
all_states = data.state.to_list()

game_is_on = True

while game_is_on:

    if answer_state == "Exit":
        states_to_learn = [states for states in all_states if states not in correct_guesses]
        # for states in all_states:
        #     if states not in correct_guesses:
        #         states_to_learn.append(states)
        print(states_to_learn)
        unknown_states = pandas.DataFrame(states_to_learn)
        unknown_states.to_csv("states_to_learn.csv")
        break

    for states_no in range(1, len(data)):
        if answer_state == data.state[states_no] and answer_state not in correct_guesses:
            new_x = data.x[states_no]
            new_y = data.y[states_no]
            writer = turtle.Turtle()
            writer.penup()
            writer.hideturtle()
            writer.goto(new_x, new_y)
            writer.write(arg=f"{answer_state}", move=False, font=("DM Sans", 10, "normal"))
            correct_guesses.append(answer_state)
    answer_state = (screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                     prompt="What's another state's name")).title()
