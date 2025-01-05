import pygame

pygame.init()

win=pygame.display.set_mode((1000,500)) 
pygame.display.set_caption("Jump & Run")

WHITE=(255,255,255)
BLACK=(0,0,0)
VIOLETT=(128,0,128)
BLAU_VIOLETT=(68,22,120)
GRASGRÜN=(63,112,77)
DUNKELROT=(139,0,0)
TÜRKIS=64,224,208

x = 250
y = 300
radius=20
vel=15
vel_x=10
vel_y=10
run=True
game_is_running=True

player_is_jumping=False

rect_height=190
rect_width=750
rect_x=0
rect_y=310
rect_boden=pygame.Rect(rect_x,rect_y,rect_width,rect_height)

font = pygame.font.Font(None,36)

def draw_game_over():
    s=pygame.Surface((1000,500), pygame.SRCALPHA)
    s.fill((0,0,0,128))
    win.blit(s,(0,0))
    text=font.render("Game Over! Please press R",True,DUNKELROT)
    text_rect = text.get_rect(center=(400,300))
    win.blit(text,text_rect)


game_over=False

while run:
    win.fill(BLAU_VIOLETT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False 

    pygame.draw.circle(win, WHITE, (int(x),int(y)), radius)
    pygame.draw.rect(win, GRASGRÜN, rect_boden)
                     
    userInput=pygame.key.get_pressed()

    if userInput[pygame.K_LEFT] and x > 0:
        x-=vel

    if userInput[pygame.K_RIGHT] and x < 1000:
        x+=vel

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

    if x > 750 and y<1100:
        y=y+10

    if y >= 500:
        game_over=True

    #if userInput[pygame.K_DOWN] and y < 500:
       #y+=vel

   # if userInput[pygame.K_UP] and y > 0:
    #    y-=vel

    if userInput[pygame.K_r] and game_over==True:
        game_over=False
        x = 250
        y = 300

    if game_over==True:
        draw_game_over()

    pygame.time.delay(20)

    pygame.display.update()