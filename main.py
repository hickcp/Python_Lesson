import turtle
#Desenhar um emoji sorridente
s = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)
def rosto(x, y, z):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(z)

rosto(-100, 100, 100)

def olho(x, y, z, d, e, a, b,):
    if e == 1:
        t.penup()
        t.goto(x - a, y + b)
        t.pendown()
        t.dot(z)
    elif d == 1:
        t.penup()
        t.goto(x + a, y + b)
        t.pendown()
        t.dot(z)
        help(turtle)



olho(-100, 100, 25, 0, 1, 35, 120,)
olho(-100, 100, 25, 1, 0, 35, 120,)

t.penup()
t.goto(-100 - 60.62, 100 + 65)
t.pendown()
t.setheading(-60)
t.circle(70,120)

input("Press any key to exit")



