import turtle
from random import randint

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("lightblue")

score = 0
high_score = 0

# write
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

# write2
pen2 = turtle.Turtle()
pen2.penup()
pen2.hideturtle()

# gameover
gv = turtle.Turtle()
gv.penup()
gv.hideturtle()

# snake
snk = turtle.Turtle()
snk.penup()
snk.speed(0)
snk.shape("square")
snk.color("green")
snk.shapesize(stretch_wid=1, stretch_len=1)
snk.goto(0, 0)

snkspeed = 10

# food
food = turtle.Turtle()
food.penup()
food.speed(0)
food.shape("circle")
food.color("red")
food.shapesize(stretch_wid=0.5, stretch_len=0.5)
food.goto(randint(-200, 0), randint(0, 200))

# apoint
apoint = turtle.Turtle()
apoint.penup()
apoint.shape("square")
apoint.shapesize(stretch_len=1, stretch_wid=1)
apoint.speed(0)
apoint.color("black")
apoint.goto(250, 0)

# apoint2
apoint2 = turtle.Turtle()
apoint2.penup()
apoint2.shape("square")
apoint2.shapesize(stretch_len=1, stretch_wid=1)
apoint2.speed(0)
apoint2.color("black")
apoint2.goto(-150, -260)

# apoint3
apoint3 = turtle.Turtle()
apoint3.penup()
apoint3.shape("square")
apoint3.shapesize(stretch_len=1, stretch_wid=1)
apoint3.speed(0)
apoint3.color("black")
apoint3.goto(-260, 260)


segments = []


def moveup():
    y = snk.ycor()
    y += snkspeed
    if y > 300:
        y = 290
    snk.sety(y)


screen.listen()
screen.onkeypress(moveup, "w")


def moveright():
    x = snk.xcor()
    x += snkspeed
    if x > 400:
        x = 390
    snk.setx(x)


screen.listen()
screen.onkeypress(moveright, "d")


def moveleft():
    x = snk.xcor()
    x -= snkspeed
    if x > 400:
        x = -390
    snk.setx(x)


screen.listen()
screen.onkeypress(moveleft, "a")


def movedown():
    y = snk.ycor()
    y -= snkspeed
    if y > 300:
        y = -290
    snk.sety(y)


screen.listen()
screen.onkeypress(movedown, "s")

while True:
    screen.update()
    if snk.distance(food) < 20:
        food.setpos(-10000, 10000)
        pen.clear()
        pen.goto(-125, 345)
        pen.write("Score: {}".format(score), align="right", font=("Courier", 25, "normal"))
        pen2.clear()
        pen2.goto(25, 345)
        pen2.write("High Score: {}".format(high_score), align="left", font=("Courier", 25, "normal"))
        score = score + 1
        high_score = score
        food.goto(randint(-290, 0), randint(0, 290))
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = snk.xcor()
        y = snk.ycor()
        segments[0].goto(x, y)
    if snk.distance(apoint) < 20:
        gv.clear()
        gv.goto(0, 0)
        gv.write("Game Over!", align="center", font=("Courier", 75, "normal"))
        pen.clear()
        pen.goto(0, -50)
        pen.write("Score: {}".format(score), align="center", font=("Courier", 25, "normal"))
        pen2.clear()
        pen2.goto(0, -100)
        pen2.write("High Score: {}".format(high_score), align="center", font=("Courier", 25, "normal"))
        snk.setpos(-10000, 10000)
    if snk.distance(apoint2) < 20:
        gv.clear()
        gv.goto(0, 0)
        pen.clear()
        pen.goto(0, -50)
        pen.write("Score: {}".format(score), align="center", font=("Courier", 25, "normal"))
        gv.write("Game Over!", align="center", font=("Courier", 75, "normal"))
        pen2.clear()
        pen2.goto(0, -100)
        pen2.write("High Score: {}".format(high_score), align="center", font=("Courier", 25, "normal"))
        snk.setpos(-10000, 10000)
    if snk.distance(apoint3) < 20:
        gv.clear()
        gv.goto(0, 0)
        pen.clear()
        pen.goto(0, -50)
        pen.write("Score: {}".format(score), align="center", font=("Courier", 25, "normal"))
        gv.write("Game Over!", align="center", font=("Courier", 75, "normal"))
        pen2.clear()
        pen2.goto(0, -100)
        pen2.write("High Score: {}".format(high_score), align="center", font=("Courier", 25, "normal"))
        snk.setpos(-10000, 10000)


screen.mainloop()
