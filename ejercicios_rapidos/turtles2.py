import turtle
from random import choice, randint

cho1 = ('red', 'green', 'blue')
cho2 = ('purple', 'pink', 'yellow')

for _ in range(1,66):
    turtle.pensize(5)
    turtle.pencolor(choice(cho1))
    turtle.forward(200)
    turtle.circle(30)
    turtle.right(30)
    turtle.fillcolor(choice(cho1))
    turtle.pencolor(choice(cho2))
    turtle.penup
    turtle.forward(50)
    turtle.right(80)
    turtle.pencolor(choice(cho2))
    turtle.penup
    turtle.forward(50)
