import pygame
import random
import sys

pygame.init()

w,h=800,600
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("Catch the falling eggs")

white=(255, 255, 255)
green=(0,255,0)
black=(0,0,0)

bowl_img=pygame.image.load("bowl.png")
egg_img=pygame.image.load("egg.png")

#Bowl and egg image
pw,ph=100,20
bowl_img=pygame.transform.scale(bowl_img,(pw,ph))
r=30
egg_img=pygame.transform.scale(egg_img,(r*2,r*2))

#Setting of bowl
bowl_x=w//2-pw//2
bowl_y=h-ph-10
bowl_speed=10

#Setting of egg
egg_x=random.randint(0,w-r*2)
egg_y=0-w
egg_speed=5

score=0
lives=3

#Font set up
font=pygame.font.Font(None,36)

#contrals frames rate
clock=pygame.time.Clock()

#Linking up the font and the text
def display_text(text,size,color,x,y):
    font=pygame.font.Font(None, size)
    rtext=font.render(text,True,color)
    screen.blit(rtext,(x,y))

running=True
game_over=False

#starting the game
while running:
        screen.fill(white)
        if game_over:
            display_text("Game over",64,(255,0,0),w//2-150,h//2-50)
            display_text(f"Final Score:{score}",36,green,w//2-100,h//2+20)
            for event in pygame.event.get():
                #when window is closed after quiting
                if event.type==pygame.QUIT:
                    running=False
                    #Restarting the game
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        score=0
                        lives=3
                        egg_speed=5
                        egg_x=random.randint(0,w-r*2)
                        egg_y=0-r
                        game_over=False
            continue
        for event in pygame.event.get():
              if event.type==pygame.QUIT:
                 running=False
                 #Events that follow when the keys get pressed
              keys=pygame.key.get_pressed()
              if keys[pygame.K_LEFT] and bowl_x>0:  
                bowl_x=bowl_speed
              egg_y+=egg_speed 
              #condition for if the egg is touching the left,right or center of the bowl.
              if(bowl_x<egg_x<bowl_x+pw or bowl_x<egg_x+r*2<bowl_x+pw) and bowl_y<egg_y+r<bowl_y+ph:
                score+=1
                egg_x=random.randint(0,w-r*2)
                egg_y=0-r
                egg_speed+=0.2
              if egg_y>h: 
               lives-=1
               egg_x=random.randint(0,w-r*2)  
               egg_y=0-r
               if lives==0:
                 game_over=True
            # Draw the player

screen.blit(bowl_img, (bowl_x, bowl_y))

# Draw the falling object

screen.blit(egg_img, (egg_x, egg_y))

# Draw the score and lives

score_text = font.render(f"Score: {score}", True, green)

lives_text = font.render(f"Lives: {lives}", True, black)

screen.blit(score_text, (10, 10))     
screen.blit(lives_text, (w - 150, 10))

# Update the screen

pygame.display.flip()

# Cap the frame rate

clock.tick(30)

# Quit Pygame

pygame.quit()

sys.exit()


                        
            