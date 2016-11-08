import pygame


#Constants
WINDOW_SIZE = (1024, 768)

def init_player():
    return {
            "position": (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2),
            "health": 100,
            "speed": (0,0),
            "angle": 0
        }


def init_gamestate():
    return {
            #Set to false when the game should exit
            "running": True,

            #The last time an asteroid was spawned
            "last_asteroid_spawn": 0,

            "player": init_player(),

            #List of asteroids in the game
            "asteroids": []
        }


def load_assets():
    background = pygame.image.load("resources/space_bg.png")
    background_scale = max(WINDOW_SIZE[0], WINDOW_SIZE[1])
    background = pygame.transform.scale(background, (background_scale, background_scale))

    

    return {
            "background": background
        }



def do_game_logic(game_state):
    pass


def draw_game(game_state, assets, screen):
    screen.blit(assets["background"], (0,0))


    pygame.display.flip()


def handle_events(game_state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state["running"] = False


def draw_translated_image(image, screen, position, scale, rotation):
    #Apply the rotation and scale we want
    scaled = pygame.transform.scale(image, scale)
    rotated = pygame.transform.rotate(scaled, rotation)

    #Calculate the center of the image
    (offset_x, offset_y) = (rotated.get_width() / 2, rotated.get_height() / 2)

    screen.blit(rotated, (position[0] - offset_x, position[1] - offset_y))


def main():
    game_state = init_gamestate()
    assets = load_assets()

    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    while game_state["running"]:
        do_game_logic(game_state)

        draw_game(game_state, assets, screen)

        handle_events(game_state)

main()

