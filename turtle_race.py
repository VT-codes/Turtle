from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle would win the race? Enter the color. ").lower()
print(f"Your bet: {user_bet}")

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.penup()
tim.goto(x=-230, y=-100)


jim = Turtle()
jim.shape("turtle")
jim.color("orange")
jim.penup()
jim.goto(x=-230, y=-50)


kyl = Turtle()
kyl.shape("turtle")
kyl.color("green")
kyl.penup()
kyl.goto(x=-230, y=0)


ney = Turtle()
ney.shape("turtle")
ney.color("yellow")
ney.penup()
ney.goto(x=-230, y=50)


leo = Turtle()
leo.shape("turtle")
leo.color("blue")
leo.penup()
leo.goto(x=-230, y=100)


go_on = True
if user_bet:
    go_on = True

while go_on:
    tim.forward(random.randint(1, 30))
    jim.forward(random.randint(1, 30))
    kyl.forward(random.randint(1, 30))
    ney.forward(random.randint(1, 30))
    leo.forward(random.randint(1, 30))

    win_tim = int(tim.xcor())
    win_jim = int(jim.xcor())
    win_kyl = int(kyl.xcor())
    win_ney = int(ney.xcor())
    win_leo = int(leo.xcor())
    coor_list = [win_leo, win_ney, win_kyl, win_jim, win_tim]

    if win_leo > 230 or win_ney > 230 or win_kyl > 230 or win_tim > 230 or win_jim > 230:
        go_on = False
    if not go_on:
        winner = max(coor_list)
        if winner == win_leo:
            print("Blue wins!")
            if user_bet == "blue":
                print("You guessed it right!")
            else:
                print("You guessed it wrong!")
        elif winner == win_ney:
            print("Yellow wins!")
            if user_bet == "yellow":
                print("You guessed it right!")
            else:
                print("You guessed it wrong!")
        elif winner == win_jim:
            print("Orange wins!")
            if user_bet == "orange":
                print("You guessed it right!")
            else:
                print("You guessed it wrong!")
        elif winner == win_tim:
            print("Red wins!")
            if user_bet == "red":
                print("You guessed it right!")
            else:
                print("You guessed it wrong!")
        elif winner == win_kyl:
            print("Green wins!")
            if user_bet == "green":
                print("You guessed it right!")
            else:
                print("You guessed it wrong!")

screen.exitonclick()
