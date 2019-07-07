import turtle

Myturtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(Myturtle, len):
    if len > 1:
        Myturtle.forward(len)
        Myturtle.right(90)
        drawSpiral(Myturtle,len-5)


drawSpiral(Myturtle, 200)
myWin.exitonclick()