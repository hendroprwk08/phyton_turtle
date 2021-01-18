#Introduction | turtle module
#“Turtle” is a Python feature like a drawing board, 
#which lets us command a turtle to draw all over it! 
#We can use functions like turtle.forward(…) and turtle.right(…) 

import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
t = turtle.Turtle()

t.forward(100) #moved skk 100 pixels forward

#kotak
for i in range(4):
    t.forward(50)
    t.right(90)

#bintang 
for i in range(5):
    t.forward(50)
    t.right(144)

#ploygon
num_sides = 6
side_length = 70
angle = 360.0 / num_sides 
 
for i in range(num_sides):
    t.forward(side_length)
    t.right(angle)

turtle.done() #the done() function and We’re done! 
