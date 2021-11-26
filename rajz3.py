import turtle
def vonal(toll,h):
    for i in range(6):
        toll.forward(h)
        toll.left(60)
        
a = turtle.Screen()
a.bgcolor("green")
a.title("vonal")
toll=turtle.Turtle()
vonal(toll,50)