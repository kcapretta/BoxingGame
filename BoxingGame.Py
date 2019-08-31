import turtle
import math
import random
import winsound
import pygame

pygame.init()
pygame.mixer.init()

# Screen set up
window = turtle.Screen()
window.bgcolor("beige")
window.title("Boxing Game")

# Images of characters
enemy_boxer = "Boxer.gif"
window.addshape(enemy_boxer)
player_boxer = "Boxer.gif"
window.addshape(space_ship)

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

# Create beginning score as zzero
score = 0

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape(player_boxer)
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15
enemyspeed = 2

# Move the player left, right, up, and down
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
    
def move_backward():
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
number_of_enemies = 1

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
    
 def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(2),2))
                         if distance < 15:
                         return True
# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-295, 275)
scorestring = "Score: %s" % score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
score_pen.hideturtle()

# Main game loop
while True:

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        # Move the enemy back and down
        if enemy.xcor() < -280 or enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            enemyspeed *= -1
        # Check for a collision between the bullet and the enemy
        if is_collision(bullet, enemy):
            winsound.PlaySound("Explosion.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

# Update Score
score += 10
scorestring = "Score: %s" %score
score_pen.clear()
score_pen.write(scorestring, False, align="left", format ??????
                
# Play background music
song = random.randint(0, 2)
if song == 0:
    sound = pygame.mixer.Sound("Star_Song.wav")
elif song == 1:
    sound = pygame.mixer.Sound("Telecom.wav")
elif song == 2:
    sound = pygame.mixer.Sound("User_Friendly_future_mix.wav")
sound.play()
                
# Add all images
enemy_boxer = "spin.gif"
window.addshape(enemy_boxer)
player_boxer = "space_ship.gif"
window.addshape(player_boxer)
  
delay = input("Press enter to finish.")
