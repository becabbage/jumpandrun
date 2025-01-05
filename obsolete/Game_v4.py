import pygame
import os

pygame.init()

# Constants, Variables etc.

WINDOW_HEIGHT=500
WINDOW_WIDTH=1000
WHITE=(255,255,255)
BLACK=(0,0,0)
x = 250
y = 250
radius=10
vel_x=10
vel_y=10

bg_img_src='resources//ocean.png'
bgn_x=0 # background x index for moving background
bgn_y=0 # background y index for later
bgn_width=1000 # background width (1000px)

game_is_running=True
player_is_jumping=False

# Resources

bg_img=pygame.image.load(bg_img_src)
bg = pygame.transform.scale(bg_img, (WINDOW_WIDTH,WINDOW_HEIGHT))


# Game Start

win=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Jump & Run")

while game_is_running:

    win.fill((BLACK))
    win.blit(bg,(bgn_x,bgn_y))
    win.blit(bg,(bgn_width+bgn_x,bgn_y))
    
    if bgn_x == -bgn_width:
        win.blit(bg,(bgn_width+1,bgn_y))
        bgn_x=0
    
    bgn_x -= 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running=False

    pygame.draw.circle(win, BLACK, (int(x),int(y)), radius)

    userInput=pygame.key.get_pressed()

    if userInput[pygame.K_LEFT] and x > 0:
        x-=vel_x

    if userInput[pygame.K_RIGHT] and x < WINDOW_WIDTH:
        x+=vel_x


    # Jumping
    if (player_is_jumping is False) and userInput[pygame.K_SPACE]:
        player_is_jumping=True

    # Jumping motion
    if player_is_jumping is True:
        y -= vel_y*3
        vel_y -= 1

        if vel_y < -10:
            player_is_jumping=False
            vel_y=10

#    if userInput[pygame.K_DOWN] and y < 500:
#        y+=vel
#
#    if userInput[pygame.K_UP] and y > 0:
#        y-=vel

    pygame.time.delay(20)

    pygame.display.update()