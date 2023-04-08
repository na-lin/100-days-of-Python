import turtle
from turtle import Screen, Turtle
import pandas

IMAGE = "blank_states_img.gif"
FONT = ('Arial', 8, 'normal')

screen = Screen()
screen.bgpic(IMAGE)
# NEW: load into screen and set turtle shape by image file
# screen.addshape(IMAGE)
# turtle.shape(IMAGE)
screen.title("U.S State Game")

write_state = Turtle()
write_state.penup()
write_state.hideturtle()

score = 0
guess_record = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
while score < 50:

    guess_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()

    if guess_state == 'Exit':

        # state_to_learn = []
        # for state in all_states:
        #     if state not in guess_record:
        #         state_to_learn.append(state)

        state_to_learn = [state for state in all_states if state not in guess_record]

        state_dict = {"state": state_to_learn}
        csv_date = pandas.DataFrame(state_dict)
        print(csv_date)
        csv_date.to_csv("state_to_learn.csv")
        # new_data = pandas.DataFrame(state_to_learn)
        # print(new_data)


        break

    if guess_state in all_states:
        state = data[data.state == guess_state]
        write_state.goto(int(state.x), int(state.y))
        write_state.write(guess_state)
        # write_state.write(state.state.item())
        score += 1
        guess_record.append(guess_state)



# turtle.mainloop()
# screen.exitonclick()
