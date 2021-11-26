import turtle
def vonal(toll,h):
    for i in range(3):
        toll.forward(h)
        toll.left(120)
        
a = turtle.Screen()
a.bgcolor("green")
a.title("vonal")
toll=turtle.Turtle()
vonal(toll,50)
