#library for graphics 
import turtle 
#draw the circles
def draw(rad,color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()

turtle.goto(-30,-280)
draw(300,'red')

turtle.goto(-30,-240)
draw(260,'white')

turtle.goto(-30,-200)
draw(220,'red')

turtle.goto(-30,-160)
draw(180,'blue')

turtle.goto(-200,75)
turtle.begin_fill()
turtle.color('white')

for x in range(5):
    turtle.forward(340)
    turtle.right(144)
turtle.end_fill()
turtle.hideturtle()
turtle.done()


