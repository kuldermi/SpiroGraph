import random
import turtle as t
from turtle import Screen
import colorgram

# colors = colorgram.extract('imgae_hirst_1.jpg')



# Making spirograph using random color
random_colors = ['blue', 'red','pink', 'green', 'yellow', 'purple']
tim = t.Turtle()
t.colormode(255)


def random_color():
    r= random.randint(0,255)
    g = random.randint ( 0, 255 )
    b = random.randint ( 0, 255 )
    return (r, g, b)

def draw_spirograph():
    tilt_angle = 5
    tim.speed(0)
    for _ in range(200):
        tim.color(random_color())
        tim.circle(80)
        tim.setheading(tilt_angle)
        tilt_angle += 5


draw_spirograph()




screen = Screen()
screen.exitonclick()