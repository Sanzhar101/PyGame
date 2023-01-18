import pygame

# initialize pygame
pygame.init()

# screen size
size = (1016, 680)
screen = pygame.display.set_mode(size)

#title
pygame.display.set_caption("My Game")

# load character and background images
character_image = pygame.image.load("character.png")
background_image = pygame.image.load("background.png")

# get character rect
character_rect = character_image.get_rect()

# set initial character position
character_rect.x = 350
character_rect.y = 450

# movement speed
speed = 5

# loop until user clicks close button
done = False

# used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # user clicked close
            done = True

    # --- Game logic 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        character_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        character_rect.x += speed

    # --- Drawing code 


    screen.blit(background_image,(0,0))

    # draw character
    screen.blit(character_image, character_rect)

   
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


pygame.quit()
