import turtle
import math
import random
import winsound
import pygame

# Screen set up
window = turtle.Screen()
window.bgcolor("beige")
window.title("Boxing Game")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-200, -200)
border_pen.pendown()
border_pen.pensize(5)
for side in range(4):
    border_pen.fd(400)
    border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score = 0

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape(space_ship)
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15
enemyspeed = 2

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -200:
        x = -200
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 200:
        x = 200
    player.setx(x)
    
def move_forward():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
    
# Create enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(3)
enemy.setposition(-100, 100)

# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

# Main game loop
while True:
  x = enemy.xcor()
  x += enemyspeed
  enemy.setx(x)
  
  if enemy.xcor() > 280:
    y = enemy.ycor()
    y -= 20
    enemyspeed *= -1
    enemy.sety(y)
    
  if enemy.xcor(x) < - 280:
    y = enemy.ycor()
    y -= 40
    enemyspeed *= -1
    enemy.sety(y)
  
  
delay = input("Press enter to finish.")
