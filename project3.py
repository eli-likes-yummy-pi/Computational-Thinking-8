import turtle

# set up
t = turtle.Turtle()
t.goto(-60,-50)
t.color("orchid")
turtle.Screen().bgcolor("black")
t.speed(1000000)
t.penup
# growing and color changing heptagon
colors = ["Navy", "DarkBlue", "MidnightBlue"]
for i  in range(100):
    t.color(colors[i % 3])
    t.forward(100 + i)
    t.left(52.428)
t.penup()
# growing and color changing octagon
t.goto(0,60)
t.color("yellow")
t.pendown()
for i in range(150):
    t.forward(30 + i)
    t.left(144)

# ending
turtle.exitonclick()
