from turtle import *

#we want to paint a house

# step 1:  draw a square 
speed(50)
width(15)
color("brown") 
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)




forward(70)
color("orange")
begin_fill()
left(90)
forward(120)    
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup()
goto(200, 200)
pendown()


color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
left(30)
forward(60)
left(90)
pendown()
forward(60)
left(90)
forward(150)


penup()
forward(30)
right(180)
forward(150)
right(90)
pendown()
forward(60)
penup()
left(90)
forward(30)
left(90)
forward(30)
left(90)
pendown()
forward(60)

penup()
forward(150)
right(90)
forward(170)
right(90)
forward(150)
right(90)
pendown()
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(180)
forward(30)
right(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)

exitonclick()
