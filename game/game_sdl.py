
#Import the rendering helper functions
import render_util

#Import SDL itself
import sdl2
import sdl2.ext

import random

#Gamestate format
#(is_running)


MAX_NOTE_TYPES = 3
BACKGROUND_SPRITE = 3

class GameState:
    def __init__(self):
        self.is_running = True
        self.notes = []

def handle_user_input(game_state):
    """
    Handle all events. This is where things like mouse and keyboard input will happen
    """

    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            game_state.is_running = False
            break

def do_game_stuff(game_state):
    if random.randint(0,3000) == 0:
        game_state.notes.append((0, random.randint(-1,1) * 100, random.randint(0,MAX_NOTE_TYPES - 1)))

    new_notes = []
    for note in game_state.notes:
        old_x, old_y, type = note

        new_notes.append((old_x - 0.1, old_y, type))
    game_state.notes = new_notes

def draw_things(game_state, renderer, sprites):
    center_x, center_y = (1024/2, 768/2)

    renderer.render_sprites([sprites[BACKGROUND_SPRITE]])

    for note in game_state.notes:
        pos_x, pos_y, type = note

        sprite = sprites[type]
        sprite.position = (int(center_x + pos_x), int(center_y + pos_y))

        renderer.render_sprites([sprite])



def main():
    game_state = GameState()

    renderer = render_util.Renderer("Python game", (1024, 768))

    sprites = [renderer.load_sprite("ghost.png"), 
            renderer.load_sprite("ghost.png"), 
            renderer.load_sprite("ghost.png"),
            renderer.load_sprite("desert.png")
        ]

    #sprite.scale = (5,5)
    #sprite.position = (500, 300)
    for sprite in sprites:
        sprite.scale = (1,1)

    sprites[0].angle = 90
    sprites[1].angle = 180
    sprites[2].angle = 0

    running = True
    while game_state.is_running:
        do_game_stuff(game_state)

        draw_things(game_state, renderer, sprites)
        #Show everything we have drawn so far on the screen
        renderer.present()

        handle_user_input(game_state)


main()


#Desert sprite from http://opengameart.org/content/seamless-desert-background-in-parts
