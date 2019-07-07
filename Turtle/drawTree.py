import turtle


myTurtle = turtle.Turtle()
myWindow = turtle.Screen()


def drawTree(myTurtle, len):
    if len > 5:
        myTurtle.forward(len)
        myTurtle.right(20)
        drawTree(myTurtle, len-15)
        myTurtle.left(40)
        drawTree(myTurtle, len-15)
        myTurtle.right(20)
        drawTree(myTurtle, len-20)
        myTurtle.backward(len)



def tree():
    myTurtle.left(90)
    drawTree(myTurtle, 100)
    myWindow.exitonclick()

tree()

