import pygame

#Initialize pygame

pygame.init()

#Set up the display

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Add a Picture")

#Load the image

image = pygame.image.load("https://th.bing.com/th/id/R.2b61de3e83a113543e156ec3986e8850?rik=xhznq1Q%2fobOMLQ&pid=ImgRaw&r=0")

#Main game loop

running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
       running = False

# Draw the image at (x, y) position
screen.blit(image, (100, 100))

# Update the display
pygame.display.flip()
# Draw the image at (x, y) position
screen.blit(image, (100, 100))

# Update the display
pygame.display.flip()
#Quit pygame

pygame.quit()