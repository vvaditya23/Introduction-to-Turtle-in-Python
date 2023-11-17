from turtle import Turtle, Screen

tt_turtle_obj = Turtle()

for _ in range(15):
    tt_turtle_obj.forward(10)
    tt_turtle_obj.penup()   #pen is up that means nothing will be written
    tt_turtle_obj.forward(10)
    tt_turtle_obj.pendown() #pen down, writing is on

screen = Screen()
screen.exitonclick()