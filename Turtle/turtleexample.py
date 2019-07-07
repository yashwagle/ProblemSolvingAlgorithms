import turtle


def turtleex():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.right(90)
    myTurtle.up()
    myTurtle.backward(50)

    myWin.exitonclick()


turtleex()
