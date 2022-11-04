import pygame
import os
from classes import Weapon
from classes import Powerups
from classes import Meteor
from classes import Spaceship
from pygame import mouse
import math

# The Frames Per Second the Program is running at:
FPS = 60

# Width and Height of the Window
WIDTH, HEIGHT = 1920, 1080

# Spaceship Dimensions
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 99, 76


# Images - Goes through the file's directory via the operating system to access these images.
ORIGINAL_SPACESHIP = pygame.image.load(os.path.join("venv", "spaceship.png"))  # Spaceship Image
ORIGINAL_BACKGROUND = pygame.image.load(os.path.join("venv", "background.jpg"))  # Background Image
ORIGINAL_LASER = pygame.image.load(os.path.join("venv", "shiplaser.png"))  # Laser Image
ORIGINAL_METEOR = pygame.image.load(os.path.join("venv", "meteorBrown_big1.png"))  # Big Meteor Image
ORIGINAL_MED_METEOR = pygame.image.load(os.path.join("venv", "meteorBrown_med1.png"))  # Medium Meteor Image
ORIGINAL_SMALL_ASTEROID = pygame.image.load(os.path.join("venv", "meteorBrown_tiny1.png"))  # Small Meteor Image


# Scales Images
SPACESHIP = pygame.transform.scale(ORIGINAL_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
BACKGROUND = pygame.transform.scale(ORIGINAL_BACKGROUND, (WIDTH, HEIGHT))
LASER = pygame.transform.scale(ORIGINAL_LASER, (SPACESHIP_WIDTH/2, SPACESHIP_HEIGHT/2))


# Creates Window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Names the title of the program
pygame.display.set_caption("Asteroids!")





# Draws Stuff on the Screen
def update(spaceship):
    # Draw a surface/sprite on the screen at the x and y coordinates provided
    WIN.blit(BACKGROUND, (0, 0))
    # Draws the Spaceship at the coordinates that the image is supposed to be according to the pygame.Rect method.
    WIN.blit(SPACESHIP, (spaceship.x, spaceship.y))

    # Makes the Spaceship face the mouse. By the way, this is not my code - I adapted it from Stack Overflow
    mouseX, mouseY = pygame.mouse.get_pos()
    playerX, playerY = spaceship.centerx, spaceship.centery

    # Fancy Math Calculation that calcuates the rotation required for the spaceship to face the mouse.
    angle = math.atan2(playerX - mouseX, playerY - mouseY)
    pygame.transform.rotate(SPACESHIP, angle)

    pygame.display.update()


# Handles Player Movement
def movement(spaceship):
    # Similar to Unity's "GetKey" or Greenfoot's "GetKeyDown"
    key_down = pygame.key.get_pressed()

    if key_down[pygame.K_a]:
        # Moves Player to the Right
        spaceship.x -= Spaceship.Speed
    if key_down[pygame.K_d]:
        # Moves Player to the Left
        spaceship.x += Spaceship.Speed
    if key_down[pygame.K_w]:
        # Moves Player Forward
        spaceship.y -= Spaceship.Speed
    if key_down[pygame.K_s]:
        # Moves Player Backwards
        spaceship.y += Spaceship.Speed


# Same as the Unity Update or Greenfoot Act Method
def main():
    # Sets Player Position - Arguments for pygame.Rect() = x, y, width, height.
    spaceship = pygame.Rect(500, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    laser = []

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
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_LSHIFT:
                    shot = pygame.Rect(spaceship.centerx,spaceship.centery + SPACESHIP_HEIGHT, 10, 5)
        movement(spaceship)
        update(spaceship)

    # Quits program
    pygame.quit()


# Makes sure that the game only runs if this file is being complied.
if __name__ == "__main__":
    main()
