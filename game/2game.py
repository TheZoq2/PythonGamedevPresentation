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

    running = True
    while running:
        #Loop through the list of events
        for event in pygame.event.get():
            #If the event tells us that the user has tried to close the window
            if event.type == pygame.QUIT: 
                running = False


main()


