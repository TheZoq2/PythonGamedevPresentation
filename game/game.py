#Import the rendering helper functions
import render_util

#Import SDL itself
import sdl2
import sdl2.ext



def main():
    renderer = render_util.Renderer("Python game", (640, 480))

    running = True
    while running:


        #Handle all events. This is where things like mouse and keyboard input will happen
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

        #Show everything we have drawn so far on the screen
        renderer.present()


main()

