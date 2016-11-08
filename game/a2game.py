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

    keys_pressed = set()

    position = 500
    running = True
    while running:
        screen.blit(background, (0, 0))

        draw_translated_image(image, screen, (position, 400), (200, 200), 0)

        pygame.display.flip()

        if pygame.K_LEFT in keys_pressed:
            position -= 1
        elif pygame.K_RIGHT in keys_pressed:
            position += 1

        #Loop through the list of events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys_pressed.add(event.key)
            elif event.type == pygame.KEYUP:
                if event.key in keys_pressed:
                    keys_pressed.remove(event.key)

            #Other events...
            if event.type == pygame.QUIT:
                running = False



main()


