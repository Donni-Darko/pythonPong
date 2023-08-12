import pygame, sys
import random

def ball_animation():
    global ball_speed_x, ball_speed_y # Makes this variable global, should make into a class
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Check to see if ball hits screen borders
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <=0 or ball.right >= width:
        ball_restart()

    # Check for Paddle Collisions
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        
def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height
    player.y += player_speed
    
def opponent_animation():
    if opponent.top <= ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >= ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= height:
        opponent.bottom = height
        
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (width / 2, height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))
    
    
pygame.init()
clock = pygame.time.Clock()

# Set up the game window
width = 1280
height = 720 # changed from 960
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Game Rectangles
ball = pygame.Rect(width/2 - 15, height/2 -15, 30, 30)
player = pygame.Rect(width - 20, height/2 - 70, 10, 140)
opponent = pygame.Rect(10, height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12') 
light_grey = (200, 200, 200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7 
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
                
    ball_animation()
    player_animation()
    opponent_animation()
    
    # Update game objects
    screen.fill(bg_color) # Clears Screen
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball) # Since sides are the same length, ellipse becomes a circle
    pygame.draw.aaline(screen,light_grey, (width/2, 0), (width/2, height))
    
    # Draw the screen
    pygame.display.flip()  # Draws updated screen
    clock.tick(60)

