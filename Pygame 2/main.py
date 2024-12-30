import pygame

pygame.init()
screen_width, screen_height = 500, 500

screen=pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("colour changing sprites")

colors={
    "red":pygame.Colour("red"),
    "green":pygame.Colour("green"),
    "blue":pygame.Colour("blue"),
    "yellow":pygame.Colour("yellow"),
    "white":pygame.Colour("white"),
}
current_color=colors["white"]

x, y=30, 30
sw, sh=60,60

clock=pygame.time.Clock()
done=False



while not done:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x-=3
    if pressed[pygame.K_RIGHT]: x+=3
    if pressed[pygame.K_UP]: y-=3
    if pressed[pygame.K_DOWN]: y+=3

    x=min(max(0,x), screen_width-sw)
    y=min(max(0,x), screen_height-sh)
    if x==0:current_color=colors["blue"]
    elif x==screen_width-sw:current_color=colors["yellow"]
    elif y==0:current_color=colors["red"]
    elif y==screen_height-sh:current_color=colors["green"]
    else:
        current_color=colors["white"]
    screen.fill((0, 0, 0,))
    pygame.draw.rect(screen, current_color,(x, y,sw,sh))
       
    pygame.display.flip()
     
    clock.tick(90) 
pygame.quit()          