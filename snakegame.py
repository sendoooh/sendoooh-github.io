from turtle import Turtle, Screen
import time
import random

print("Welcome to Snakegame! ")

screen = Screen()
screen.bgcolor("Green")
screen.setup(width=600, height=600)
screen.tracer(False)

head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

score = 0
highest_score = 0

score_sign = Turtle("turtle")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write("Score: 0 / Highscore: 0 ", align="center", font=("Arial", 18))


body_part = []


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
def move_up():
    if head.direction != "down":
        head.direction = "up"  # chyba ne == ale =. == if

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_left():
    if head.direction != "right":
        head.direction = "left"

screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")

while True:
    screen.update()

    if head.xcor() > 290 or head.xcor() < - 290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1.5)
        head.goto(0, 0)
        head.direction = "stop"
        print("you died")

        for one_body_part in body_part:
            one_body_part.goto(1500, 1500)

        body_part.clear()

        score = 0
        
        score_sign.clear()
        score_sign.write(f"Score:{score} / Highscore:{highest_score} ", align="center", font=("Arial", 18))

    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)

        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_part.append(new_body_part)

        score += 10

        score_sign.clear()
        if score > highest_score:
            highest_score = score
        score_sign.write(f"Score:{score} / Highscore:{highest_score} ", align="center", font=("Arial", 18))


    for index in range(len(body_part) -1, 0, -1):
        x = body_part[index - 1].xcor()
        y = body_part[index - 1].ycor()
        body_part[index].goto(x, y)

    if len(body_part) > 0:
        x = head.xcor()
        y = head.ycor()
        body_part[0].goto(x, y)
    
    move()

    for one_body_part in body_part:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"
            print("you died")

            for one_body_part in body_part:
                one_body_part.goto(1500, 1500)

            body_part.clear()

    time.sleep(0.1)

screen.exitonclick()
