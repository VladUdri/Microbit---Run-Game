from microbit import *
import random

x = 50
fall = 0
score = 0
pos = 2
counter = 0
verif = 0

DELAY = 20
SHIFT_WALL_LVL_1 = 30
NEW_WALL_LVL_1 = 150
COUNTS_PER_SCORE_LVL_1 = 150

SHIFT_WALL_LVL_2 = 20
NEW_WALL_LVL_2 = 100
COUNTS_PER_SCORE_LVL_2 = 100

SHIFT_WALL_LVL_3 = 10
NEW_WALL_LVL_3 = 50
COUNTS_PER_SCORE_LVL_3 = 50

def make_pipe():
	i = Image("22222:00000:00000:00000:00000")
	gap = random.randint(0,3)
	i.set_pixel(gap, 0, 0)
	return i

i = make_pipe()
	

while True:
	if counter == 0:
		display.scroll("Get ready!")
	counter += 1
	display.show(i)

	if button_a.was_pressed():
		pos -= 1
	if button_b.was_pressed():
		pos += 1
	if pos < 0:
		pos = 0
	if pos > 4:
		pos = 4
	fall += 1
	if fall > 2:
		fall = 2

		x += fall

	if x > 99:
		x = 99
	if x < 0:
		x = 0

	led_x = int(x / 20)
	display.set_pixel(pos, led_x, 9)

	if i.get_pixel(pos, 4) != 0:				# if the player hits the wall shows sad img + score
		display.show(Image.SAD)
		sleep(500)
		display.scroll("Score: " + str(score))
		break	
	
	if score <= 4:
		if score == 0 and verif == 0:
			display.scroll("Lvl: 1")
			verif = 1

		if(counter % SHIFT_WALL_LVL_1 == 0):
			i = i.shift_down(1)

		if(counter % NEW_WALL_LVL_1 == 0):
			i = make_pipe()

		if(counter % COUNTS_PER_SCORE_LVL_1 == 0):
			score += 1

	if score > 4 and score <= 16:
		if score == 5 and verif == 1:
			display.scroll("Lvl: 2")
			verif = 2

		if(counter % SHIFT_WALL_LVL_2 == 0):
			i = i.shift_down(1)

		if(counter % NEW_WALL_LVL_2 == 0):
			i = make_pipe()

		if(counter % COUNTS_PER_SCORE_LVL_2 == 0):
			score += 2

	if score > 16:
		if score == 17 and verif == 2:
			display.scroll("Lvl: 3")
			verif = 3

		if(counter % SHIFT_WALL_LVL_3 == 0):
			i = i.shift_down(1)

		if(counter % NEW_WALL_LVL_3 == 0):
			i = make_pipe()

		if(counter % COUNTS_PER_SCORE_LVL_3 == 0):
			score += 3

	sleep(20)

