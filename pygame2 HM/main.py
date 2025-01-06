import pygame

pygame.init()
screen_width, screen_height = 500, 500

screen=pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("colour changing sprites")

colors={
    "red":pygame.Color("red"),
    "green":pygame.Color("green"),
    "blue":pygame.Color("blue"),
    "yellow":pygame.Color("yellow"),
    "white":pygame.Color("white"),
}
current_color=colors["white"]

# ask
x, y=30, 30
cr=20
clock=pygame.time.Clock()
done=False



while not done:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
           done=True

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x -=3
    if pressed[pygame.K_RIGHT]: x +=3
    if pressed[pygame.K_UP]: y -=3
    if pressed[pygame.K_DOWN]: y +=3

# ask
    x=min(max(0,x), screen_width-cr)
    y=min(max(0,y), screen_height-cr)

# ask
    if x==0:
        current_color=colors["blue"]
        screen.fill((255,0,0))
    elif x==screen_width-cr:
        current_color=colors["yellow"]
        screen.fill((105,6,90))
    elif y==0:
        current_color=colors["red"]
        screen.fill((79,99,5))
    elif y==screen_height-cr:
        current_color=colors["green"]
        screen.fill((25,60,1))
    else:
        current_color=colors["white"]
        screen.fill((0,0,0))
    #screen.fill((0, 0, 0,))

# ask teacher
    pygame.draw.circle(screen, current_color,(x, y,cr))
       
    pygame.display.flip()
     
    clock.tick(90) 


pygame.quit()