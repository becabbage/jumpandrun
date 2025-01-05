import pygame

pygame.init()

win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Jump & Run")

WHITE=(255,255,255)
BLACK=(0,0,0)
x = 250
y = 250
radius=10
vel_x=10
vel_y=10

game_is_running=True
player_is_jumping=False

while game_is_running:

    win.fill((BLACK))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running=False

    pygame.draw.circle(win, WHITE, (int(x),int(y)), radius)

    userInput=pygame.key.get_pressed()

    if userInput[pygame.K_LEFT] and x > 0:
        x-=vel_x

    if userInput[pygame.K_RIGHT] and x < 500:
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