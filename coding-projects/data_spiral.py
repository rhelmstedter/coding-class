#!python3

###########################################
# Try changing the number of sides or the 
# distance on lines 12 and 13. Replace the
# color on line 16 and see what happens. 
###########################################

import turtle
screen = turtle.Screen()
screen.bgcolor(4,99,194)
turtle.speed(0)

sides = 3
distance = 3

for _ in range(100*sides):
  turtle.color('white')
  distance += 3
  turtle.forward(distance)
  turtle.right(360/sides+1)
