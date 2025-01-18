import pygame
import random
import sys

pygame.init()

# Screen dimensions
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Save the Falling People")

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)

# Images with error handling
try:
    c_img = pygame.image.load("c.png")
    p_img = pygame.image.load("p.png")
except pygame.error:
    print("Image file not found!")
    sys.exit()

# Resize images
pw, ph = 100, 20
c_img = pygame.transform.scale(c_img, (pw, ph))
r = 30
p_img = pygame.transform.scale(p_img, (r * 2, r * 2))

# Car settings
c_x = w // 2 - pw // 2
c_y = h - ph - 10
c_speed = 10

# Person settings
p_x = random.randint(0, w - r * 2)
p_y = -r
p_speed = 5

# Score and lives
score = 0
lives = 3

# Font setup
font = pygame.font.Font(None, 36)

# Control frame rate
clock = pygame.time.Clock()

# Function to display text
def display_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect(center=(x, y))
    screen.blit(rendered_text, text_rect)

running = True
game_over = False

# Game loop
while running:
    screen.fill(white)

    if game_over:
        display_text("Game Over", 64, (255, 0, 0), w // 2, h // 2 - 50)
        display_text(f"Final Score: {score}", 36, green, w // 2, h // 2 + 20)
        display_text("Press 'R' to Restart", 36, black, w // 2, h // 2 + 60)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                score = 0
                lives = 3
                p_speed = 5
                p_x = random.randint(0, w - r * 2)
                p_y = -r
                c_x = w // 2 - pw // 2
                c_y = h - ph - 10
                game_over = False
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and c_x > 0:
        c_x -= c_speed
    if keys[pygame.K_RIGHT] and c_x < w - pw:
        c_x += c_speed

    p_y += p_speed

    if (c_x < p_x < c_x + pw or c_x < p_x + r * 2 < c_x + pw) and c_y < p_y + r < c_y + ph:
        score += 1
        p_x = random.randint(0, w - r * 2)
        p_y = -r
        p_speed += 0.2

    if p_y > h:
        lives -= 1
        p_x = random.randint(0, w - r * 2)
        p_y = -r
        if lives == 0:
            game_over = True

    screen.blit(c_img, (c_x, c_y))
    screen.blit(p_img, (p_x, p_y))

    score_text = font.render(f"Score: {score}", True, green)
    lives_text = font.render(f"Lives: {lives}", True, black)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (w - 150, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()




