import turtle

turtle.Screen().bgcolor("Orange")

sc = turtle. Screen()
sc.setup(400, 300)

turtle. title("Welcome to the Square Window!")

pen = turtle. Turtle()
#Square
pen.forward(100)
pen.left(90)
pen.forward(100)
pen. left(90)
pen.forward(100)
pen.right(90)
pen.backward(100)

turtle.done()


import turtle

turtle.Screen().bgcolor("Hotpink")

sc = turtle. Screen()
sc.setup(400, 300)

turtle. title("Welcome to the Triangle  Window!")

pen = turtle. Turtle()
# Triangle
pen.forward(100)
pen.left(120)
pen.forward(100)
pen. left(120)
pen.forward(100)

turtle.done()


import turtle

turtle.Screen().bgcolor("Yellow")
pen = turtle.Turtle()

#first triangle for star 

pen.forward(100) #draw base
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.penup()
pen.right(150)
pen.forward(50)


#second triangle for star 

pen.pendown()
pen.right(90)
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.right(100)
pen.forward(100)

turtle.done() 

