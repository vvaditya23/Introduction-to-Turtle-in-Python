import random
from turtle import Turtle, Screen

turtle = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

for _ in range(200):
    turtle.color(random.choice(colors))
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()