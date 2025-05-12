# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
# TODO - create your player character
s1 = create_sprite("orangesquare",-100,0)
s2 = create_sprite("bluesquare2", 100,0)
# TODO - set your background
set_background("grid")
# TODO - set the starting value for your variable
time=0


# Section 3: Controls
# TODO - define your controls
def move_up():
	s1.setheading(90)
def move_up2():
	s2.setheading(90)
def move_down():
	s1.setheading(270)
def move_down2():
	s2.setheading(270)
def move_left():
	s1.setheading(180)
def move_left2():
	s2.setheading(180)
def move_right():
	s1.setheading(0)
def move_right2():
	s2.setheading(0)
# TODO - pick keys for each control
window.onkeypress(move_up,"Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(move_up2, "w")
window.onkeypress(move_down2, "s")
window.onkeypress(move_left2, "a")
window.onkeypress(move_right2, "d")
# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  
	 
    
 	# TODO - code for automatic actions






	window.update()

	# if :
	# 	break
	

print("Game Over")

