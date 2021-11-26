import turtle
def vonal(toll,h):
    for i in range(4):
        toll.forward(h)
        toll.left(90)
        
a = turtle.Screen()
a.bgcolor("green")
a.title("vonal")
toll=turtle.Turtle()
vonal(toll,50)