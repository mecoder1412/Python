import pygame  # Import the Pygame library for game development
import random  # Import the random module for generating random values

pygame.init()  # Initialize Pygame

# Set up the game window
screen = pygame.display.set_mode((600, 400))  # Create a 600x400 pixel window
pygame.display.set_caption("Shoot the enemies")  # Set the window title
clock = pygame.time.Clock()  # Create a clock object to control the game's frame rate

# Score
score = 0

# Load and scale images
pimg = pygame.image.load("t.png")  # Load the player (fire truck) image
pimg = pygame.transform.scale(pimg, (60, 60))  # Resize fire truck

eimg = pygame.image.load("f.png")  # Load the enemy image
eimg = pygame.transform.scale(eimg, (50, 50))  # Resize enemy

bimg = pygame.image.load("w.png")  # Load the bullet (fire) image
bimg = pygame.transform.scale(bimg, (20, 40))  # Resize fire

bg = pygame.image.load("bg.png")  # Load the background image
bg = pygame.transform.scale(bg, (600, 400))  # Resize background

# Player attributes
px = 270  # Initial x-coordinate of the player
py = 330  # Initial y-coordinate of the player
pch = 0   # Player movement change (left/right)

# Enemy attributes
n = 5  # Number of enemies
ex = [random.randint(0, 550) for _ in range(n)]  # Enemy x-coordinates
ey = [random.randint(50, 150) for _ in range(n)]  # Enemy y-coordinates
xch = [4 for _ in range(n)]  # Enemy movement speed (x-direction)
ych = [40 for _ in range(n)]  # Enemy movement speed (y-direction)

# Bullet attributes
bx = 0  # Bullet x-coordinate
by = py  # Bullet y-coordinate (starts at player)
byc = 10  # Bullet speed
bs = "ready"  # Bullet state: "ready" means it can be fired

# Function to draw the player
def player(x, y):
    screen.blit(pimg, (x, y))

# Function to draw an enemy
def enemy(x, y):
    screen.blit(eimg, (x, y))

# Function to draw the bullet
def fire_bullet(x, y):
    global bs
    bs = "fire"
    screen.blit(bimg, (x + 20, y - 20))  # Adjusted to match new sizes

# Function to check for collisions
def is_collision(ex, ey, bx, by):
    return abs(ex - bx) < 30 and abs(ey - by) < 30  # Adjusted collision range

# Function to show score
def show_score():
    font = pygame.font.Font(None, 35)
    rtext = font.render(f"Score: {score}", True, (255, 255, 255))  # White color
    screen.blit(rtext, (10, 10))

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pch = -5
            if event.key == pygame.K_RIGHT:
                pch = 5
            if event.key == pygame.K_SPACE and bs == "ready":
                bx = px
                by = py  # Bullet fires from the player position
                fire_bullet(bx, by)

        # Key released
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                pch = 0

    # Player Movement
    px += pch
    px = max(0, min(px, 540))  # Keep player within screen bounds

    # Enemy Movement
    for i in range(n):
        ex[i] += xch[i]
        if ex[i] <= 0 or ex[i] >= 550:
            xch[i] *= -1
            ey[i] += ych[i]

        # Check collision
        if is_collision(ex[i], ey[i], bx, by):
            by = py
            bs = "ready"
            score += 1
            ex[i] = random.randint(0, 550)
            ey[i] = random.randint(50, 150)

        # Draw enemy
        enemy(ex[i], ey[i])

    # Bullet Movement
    if bs == "fire":
        fire_bullet(bx, by)
        by -= byc
        if by < 0:
            bs = "ready"

    # **Game Over Condition: If bullet passes the player**
    if by > py:
        print("Game Over!")
        running = False

    # Draw Player and Score
    player(px, py)
    show_score()

    pygame.display.update()
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()

    







        

