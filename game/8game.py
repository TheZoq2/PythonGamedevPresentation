#Importing libraries
import pygame

import random


def draw_translated_image(image, screen, position, scale, rotation):
    #Apply the rotation and scale we want
    scaled = pygame.transform.scale(image, scale)
    rotated = pygame.transform.rotate(scaled, rotation)

    #Calculate the center of the image
    (offset_x, offset_y) = (rotated.get_width() / 2, rotated.get_height() / 2)

    screen.blit(rotated, (position[0] - offset_x, position[1] - offset_y))


def main():
    """
    The main game code
    """
    #Initializing pygame 
    pygame.init()

    #Creating a window
    WINDOW_SIZE = (1024, 768)
    screen = pygame.display.set_mode(WINDOW_SIZE)

    image = pygame.image.load("resources/ghost.png")
    background = pygame.image.load("resources/background.png")

    angle = 0
    running = True
    while running:
        screen.blit(background, (0, 0))

        draw_translated_image(image, screen, (200, 200), (300, 300), angle)
        angle += 0.5

        pygame.display.flip()

        #Loop through the list of events
        for event in pygame.event.get():
            #If the event tells us that the user has tried to close the window
            if event.type == pygame.QUIT: 
                running = False



main()


