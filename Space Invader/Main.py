import pygame  # Import the Pygame library for game development
import random  # Import the random module for generating random values

pygame.init()  # Initialize Pygame

# Set up the game window
screen = pygame.display.set_mode((600, 400))  # Create a 600x400 pixel window
pygame.display.set_caption("Shoot the enemies")  # Set the window title
clock = pygame.time.Clock()  # Create a clock object to control the game's frame rate

# Load game images
pimg = pygame.image.load("rocket.png")  # Load the player (rocket) image
eimg = pygame.image.load("eneny.png")   # Load the enemy image
bimg = pygame.image.load("bull.png")    # Load the bullet image
bg = pygame.image.load("bg.png")        # Load the background image

# Player initial position and movement
px = 370  # Initial x-coordinate of the player
py = 500  # Initial y-coordinate of the player
pch = 0   # Player movement change (left/right)

# Enemy attributes
n = 5  # Number of enemies
ex = []  # List to store enemy x-coordinates
ey = []  # List to store enemy y-coordinates
xch = [] # List to store enemy movement change in x-direction
ych = [] # List to store enemy movement change in y-direction

# Initialize enemy positions and movement
for _ in range(n):
    ex.append(random.randint(0, 576))  # Random x-position within screen width
    ey.append(random.randint(50, 150)) # Random y-position within a range
    xch.append(4)   # Speed of enemy movement along x-axis
    ych.append(40)  # Speed of enemy movement downwards when hitting the screen boundary

# Bullet attributes
bx = 0  # Initial x-coordinate of the bullet
by = 500  # Initial y-coordinate of the bullet (same as player position)
byc = 10  # Bullet speed along the y-axis
bs = "ready"  # Bullet state: "ready" means bullet can be fired

# Function to draw the player at given coordinates
def player(x, y):
    screen.blit(pimg, (x, y))  # Draw player image at specified position

# Function to draw an enemy at given coordinates
def enemy(x, y):
    screen.blit(eimg, (x, y))  # Draw enemy image at specified position

# Function to draw the background
def screen_bg(x, y):
    screen.blit(bg, (x, y))  # Draw background image at specified position
    # Function to draw the bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bimg, (x+16, y-10))  # Draw bullet image at specified position

def is_collision(ex,ey,bx,by):
  (ex-bx)<27 and abs(ey-by)<27 

#game loop
running=True
while running:
    screen.fill((0,0,0))

#check event
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

#key pressed
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pch=-5
            if event.key==pygame.K_RIGHT:
                pch=5
            if event.key==pygame.K_SPACE and bs=="ready":
                bx=px
                fire_bullet(bx,by)

#key released
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
              pch=0 
    #Player Movement
    px+=pch
    px=max(0,min(px,736))#stay with in the screen

    #enemy movement
    for i in range(n):
        ex[i]+=xch[i]
        if ex[i]<= 0 or ex[i]>= 736:
            xch[i]*=-1
        ey[i]+=ych[i]

    #check collision
        if is_collision(ex  [i],ey[i],bx,by):
          by=500
          bs="ready"
          ex[i]=random.randint(0,736)
          ey[i]=random.randint(50,150)

    #Draw enemy
        enemy(ex[i],ey[i])

    #bullet movement
    if bs=="fire":
        fire_bullet(bx,by)
        by-=ych
        if by<0:
            by=500
            bs="ready"

    #draw player
    player(px,py)

    pygame.display.flip()
    clock.tick(60)#limit to 60 frames per second
pygame.quit()               

    







        

