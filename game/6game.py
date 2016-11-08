#Importing libraries
import pygame

import random



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

    position = 0
    running = True
    while running:
        screen.blit(background, (0, 0))

        screen.blit(image, (position, 100))

        position += 0.2

        pygame.display.flip()

        #Loop through the list of events
        for event in pygame.event.get():
            #If the event tells us that the user has tried to close the window
            if event.type == pygame.QUIT: 
                running = False



main()


