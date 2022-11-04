import pygame
import os


# The Frames Per Second the Program is running at:
FPS = 60

# Width and Height of the Window
WIDTH, HEIGHT = 1000, 500

# Images - Goes through the file's directory via the operating system to access this image.
ORIGINAL_SPACESHIP_IMAGE = pygame.image.load(os.path.join("venv", "spaceship.png"))
ORIGINAL_BACKGROUND_IMAGE = pygame.image.load(os.path.join("venv", "background.png"))
ORIGINAL_LASER_IMAGE = pygame.image.load(os.path.join("venv", "shiplaser.png"))


# Spaceship Dimensions
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 99, 76

# Scales Images
SPACESHIP_IMAGE = pygame.transform.scale(ORIGINAL_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
BACKGROUND_IMAGE = pygame.transform.scale(ORIGINAL_BACKGROUND_IMAGE, (WIDTH, HEIGHT))
LASER_IMAGE = pygame.transform.scale(ORIGINAL_LASER_IMAGE, (SPACESHIP_WIDTH/2, SPACESHIP_HEIGHT/2))


# Creates Window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Names the title of the program
pygame.display.set_caption("Asteroids V1.0")

# Speed of the Spaceship
SPEED = 5
# Bullet Speed
BULLET_SPEED = 5
# Max Ammo
MAX_AMMO = 5


# Draws Stuff on the Screen
def draw(spaceship):
    # Draw a surface/sprite on the screen at the x and y coordinates provided
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    # Draws the Spaceship at the coordinates that the image is supposed to be according to the pygame.Rect method.
    WIN.blit(SPACESHIP_IMAGE, (spaceship.x, spaceship.y))
    pygame.display.update()


# Handles Player Movement
def movement(spaceship):
    # Similar to Unity's "GetKey" or Greenfoot's "GetKeyDown"
    key_down = pygame.key.get_pressed()

    if key_down[pygame.K_a]:
        # Moves Player to the Right
        spaceship.x -= SPEED
    if key_down[pygame.K_d]:
        # Moves Player to the Left
        spaceship.x += SPEED
    if key_down[pygame.K_w]:
        # Moves Player Forward
        spaceship.y -= SPEED
    if key_down[pygame.K_s]:
        # Moves Player Backwards
        spaceship.y += SPEED


# Same as the Unity Update or Greenfoot Act Method
def main():
    # Sets Player Position - Arguments for pygame.Rect() = x, y, width, height.
    spaceship = pygame.Rect(500, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    bullets = []

    # Clock that maintains FPS
    clock = pygame.time.Clock()
    # If this boolean is true, then the program runs.
    run = True
    while run:
        clock.tick(FPS)
        # Loops through this check until the user decides to quit the program, then the code in the loop will run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Handles Shooting
            # if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_LCTRL and len(bullets) < MAX_AMMO:
                # bullets.append(laser)
        # handle_weapons(bullets)
        movement(spaceship)
        draw(spaceship)

    # Quits program
    pygame.quit()


# Makes sure that the game only runs if this file is being complied.
if __name__ == "__main__":
    main()
