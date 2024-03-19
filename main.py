import turtle
import pandas
import pyarrow

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# # # get coordinates of the mouse on the screen/game window:
# # only required to get coordinate to generate the "50_states.csv" file
# # once that is done, this block of code will be commented out or deleted
# def get_mouse_click_coor(x, y):
# 	print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# # we have to replace screen.exitonclick() with code below to keep window open (or comment it out)
# turtle.mainloop()
# # #

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
	# # get answer from player:
	answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Do you know another state?").title()
	if answer_state == "Exit":
		missing_states = [state for state in all_states if state not in guessed_states]
		# missing_states = []
		# for state in all_states:
		# 	if state not in guessed_states:
		# 		missing_states.append(state)
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("states_to_learn.csv")
		break
	if answer_state in all_states:
		guessed_states.append(answer_state)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = data[data.state == answer_state]
		t.goto(int(state_data.x), int(state_data.y))
		t.write(answer_state)
	else:
		print("WRONG...")

