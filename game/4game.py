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

    angle = 0
    running = True
    while running:
        #The original image
        screen.blit(image, image.get_rect())

        #A moved image
        screen.blit(image, (100, 100))

        #A rotated version of the image
        rotated = pygame.transform.rotate(image, 45)
        screen.blit(rotated, (400, 100))

        #A scaled version of the image
        scaled = pygame.transform.scale(image, (400, 400))
        screen.blit(scaled, (700, 100))

        pygame.display.flip()

        #Loop through the list of events
        for event in pygame.event.get():
            #If the event tells us that the user has tried to close the window
            if event.type == pygame.QUIT: 
                running = False



main()


