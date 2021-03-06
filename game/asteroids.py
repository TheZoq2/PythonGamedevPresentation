import pygame
import math
import time
import random

"""
A demo game showing of some of the things I talked about during the presentation.

This should probably be split into more files as there are a lot of functions
"""



"""
Utility functions:
"""
def draw_translated_image(image, screen, position, scale, rotation):
    """
    Draws the specified image to the screen at the specified angle and scale
    with the center point at `position`
    """
    # Apply the rotation and scale we want
    scaled = pygame.transform.scale(image, scale)
    rotated = pygame.transform.rotate(scaled, rotation)

    # Calculate the center of the image
    (offset_x, offset_y) = (rotated.get_width() / 2, rotated.get_height() / 2)

    screen.blit(rotated, (position[0] - offset_x, position[1] - offset_y))


def calculate_angle_between_points(point1, point2):
    """
    Calculates the angle between two points in space using some trigonometry

    Negating the y axis might be the wrong way of doing things but im too tired
    to remember the correct way right now
    """
    difference_x = point2[0] - point1[0]
    difference_y = -(point2[1] - point1[1])

    angle = math.atan2(difference_y, difference_x)

    return angle


def rad_to_deg(rad):
    """
    Converts a value in radians to a value in degrees
    """
    return rad / math.pi * 180


def direction_from_angle(angle, length):
    """
    Returns the x and y coordinates that you would get if you draw a line
    of 'length' length at an angle 'angle'. This can be used if you want to move
    something along an angle with a ceratin speed

    angle is in radians

    This uses the same "coordinate system" as the result of the calculate_angle_between_points function,
    hence the - sign.
    """

    return (math.cos(angle) * length, -math.sin(angle) * length)



def add_2d_tuples(tup1, tup2):
    """
    Returns the sum of each element of 2 2d tuples
    """
    (x1, y1) = tup1
    (x2, y2) = tup2
    
    return (x1 + x2, y1 + y2)


def multiply_2d_tuple(tup, val):
    """
    Multiplies each element of a 2d tuple with a value
    """
    (x,y) = tup

    return (x * val, y * val)

def sub_2d_tuples(tup1, tup2):
    """
    Subtracts each element in tup2 from tup1

    tup1 and 2 are expected to contain 2 elements
    """
    (x1, y1) = tup1
    (x2, y2) = tup2
    
    return (x1 - x2, y1 - y2)


def tuple_length(tup):
    """
    Calculates the length of a tuple interpreted as a 2d vector using the
    pythagorean theorem
    """
    (x,y) = tup
    return math.sqrt(x ** 2 + y ** 2)





"""
Game functions:
"""


# Constants
WINDOW_SIZE = (1024, 768)

SHIP_ACCELERATION = 80
SHIP_SIZE = (48, 48)
SHOT_SIZE = (16, 16)

# The time in seconds beween shots
FIRING_RATE = 0.5

BULLET_SPEED = 200

# The time between a bullet being shot and it getting removed
BULLET_DESPAWN_TIME = 2


ASTEROID_SPAWN_RADIUS = 650
ASTEROID_DESPAWN_RADIUS = 700
ASTEROID_AMOUNT = 10
ASTEROID_RADIUS = 64


def init_player():
    """
    Creates a new player object that is stored as a dictionary
    """
    return {
            "position": (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2),
            "health": 100,
            "speed": (0,0),
            # The player angle in radians. Make sure to convert to degrees when 
            # drawing with pygame
            "angle": 0, 
            # The time in seconds since the last shot 
            "last_shot_time": 0,
        }


def init_gamestate():
    """
    Creates a new game state dictionary
    """

    return {
            # Set to false when the game should exit
            "running": True,

            # The last time an asteroid was spawned
            "last_asteroid_spawn": 0,

            "player": init_player(),

            # List of asteroids in the game
            "asteroids": [],

            # List of bullets in the game
            "bullets": []
        }


def new_asteroid():
    """
    Spawns a new asteroid with a random velocity and a random point outside the screen
    """
    center = multiply_2d_tuple(WINDOW_SIZE, 0.5)

    # Generate a random angle
    angle = random.random() * math.pi * 2
    # use that angle to generate xy coordinates at ASTEROID_SPAWN_RADIUS
    # around the center of the screen
    offset = (math.cos(angle), math.sin(angle))
    position = add_2d_tuples(center, multiply_2d_tuple(offset, ASTEROID_SPAWN_RADIUS))

    velocity_angle = random.random() * math.pi * 2
    velocity = (math.cos(velocity_angle), math.sin(velocity_angle))

    return {
        "position": position,
        "velocity": velocity
    }



def add_bullet(game_state, position, speed):
    """
    Adds a bullet to the game at a certain position and speed
    """
    bullet = {
            "position": position,
            "speed": speed,
            "start_time": time.time()
        }

    game_state["bullets"].append(bullet)


def remove_dead_bullets(game_state):
    """
    Removes any bulets that have existed for longer than BULLET_DESPAWN_TIME
    """
    despawn_criteria = (lambda bullet: 
        True if time.time() - bullet["start_time"] > BULLET_DESPAWN_TIME else False)

    game_state["bullets"] = [bullet for bullet in game_state["bullets"] if not despawn_criteria(bullet)]


def rotate_player_to_point(player, point):
    """
    Updates the angle value of the player so that the ship points towards that point
    """

    angle = calculate_angle_between_points(player["position"], point)

    player["angle"] = angle


def load_assets():
    """
    Loads all images used by the draw_game function. You could also load
    sounds here if you decide to use them

    Assets, like the gamestate are stored in a dictionary for easy modifcation,
    passing around and lookup
    """
    # Loading the background and scaling it so it fills the whole window
    background = pygame.image.load("resources/background.png")
    background_scale = max(WINDOW_SIZE[0], WINDOW_SIZE[1])
    background = pygame.transform.scale(background, (background_scale, background_scale))

    ship = pygame.image.load("resources/ship.png")

    bullet = pygame.image.load("resources/shot.png")

    asteroid = pygame.image.load("resources/asteroid.png")

    return {
            "background": background,
            "ship": ship,
            "bullet": bullet,
            "asteroid": asteroid
        }


def asteroid_despawn_condition(asteroid):
    """
    Predicate applied to check wether or not to remove an asteroid from the game.

    Returns True if the asteroid should remain in the game, False otherwise
    """
    center = multiply_2d_tuple(WINDOW_SIZE, 0.5)
    return tuple_length(sub_2d_tuples(asteroid["position"], center)) < ASTEROID_DESPAWN_RADIUS

def update_asteroid(asteroid):
    """
    Updates the location of a given asteroid based on its velocity
    """
    asteroid["position"] = add_2d_tuples(asteroid["position"], asteroid["velocity"])
    return asteroid


def manage_asteroids(game_state):
    """
    Updates, removes and adds asteroids
    """
    # Despawn asteroids that are too far away
    game_state["asteroids"] = list(filter(asteroid_despawn_condition, game_state["asteroids"]))

    # Update the remaining positions
    game_state["asteroids"] = list(map(update_asteroid, game_state["asteroids"]))

    asteroids_to_add = ASTEROID_AMOUNT - len(game_state["asteroids"])

    for _ in range(asteroids_to_add):
        game_state["asteroids"].append(new_asteroid())


def do_hit_detection(game_state):
    """
    Checks for asteroids<-> bullet collision and removes them accordingly
    """
    for asteroid in game_state["asteroids"]:
        for bullet in game_state["bullets"]:
            difference = sub_2d_tuples(asteroid["position"], bullet["position"])

            if tuple_length(difference) < ASTEROID_RADIUS:
                game_state["asteroids"].remove(asteroid)
                game_state["bullets"].remove(bullet)




def do_game_logic(game_state, delta_t):
    """
    Updates the game and performs things like moving the ship, moving asteroids
    and checking bullet collision

    delta_t is a time value to multiply all movement with. This value is equal to the
    time the last iteration of the game loop took which ensures smooth movement
    on slower or faster hardware
    """

    # Updating the player position
    player = game_state["player"]

    # Add the current speed of the ship to the position
    player["position"] = add_2d_tuples(
                    player["position"],
                    multiply_2d_tuple(player["speed"],delta_t)
                )



    do_hit_detection(game_state)
    manage_asteroids(game_state)

    # Updating the position of all the bullets
    for bullet in game_state["bullets"]:
        bullet["position"] = add_2d_tuples(
                bullet["position"],
                multiply_2d_tuple(bullet["speed"], delta_t)
            )

    remove_dead_bullets(game_state)


def draw_game(game_state, assets, screen):
    """
    Draws the current gamestate to the screen
    """
    # Draw the background
    screen.blit(assets["background"], (0,0))

    # Draw all the bullets
    # This is done before drawing the ship so they apear under it
    for bullet in game_state["bullets"]:
        draw_translated_image(assets["bullet"], screen, bullet["position"], SHOT_SIZE, 0)

    # Draw the ship where it is right now
    player = game_state["player"]
    draw_translated_image(assets["ship"], screen, player["position"], SHIP_SIZE, rad_to_deg(player["angle"]))

    # Draw all the asteroids
    for asteroid in game_state["asteroids"]:
        size = (ASTEROID_RADIUS, ASTEROID_RADIUS)
        draw_translated_image(assets["asteroid"], screen, asteroid["position"], size, 0)

    pygame.display.flip()


def handle_events(game_state, keys_pressed, delta_t):
    """
    Handles all pygame events

    delta_t is a time value to multiply all movement with. This value is equal to the
    time the last iteration of the game loop took which ensures smooth movement
    on slower or faster hardware
    """

    # Getting the player from the gamestate struct since we will modify it a lot here
    player = game_state["player"]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state["running"] = False

        # When the mouse is moved, the ship should be pointed towards it
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            rotate_player_to_point(player, mouse_pos)

        # Keeping track of what keys are being held
        if event.type == pygame.KEYDOWN:
            keys_pressed.add(event.key)
        if event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed.remove(event.key)

    
    # Updating keyboard
    if pygame.K_w in keys_pressed:
        # Add some speed in the current direction of the ship
        (old_vel_x, old_vel_y) = player["speed"]

        (add_vel_x, add_vel_y) = direction_from_angle(player["angle"], delta_t * SHIP_ACCELERATION)

        player["speed"] = (old_vel_x + add_vel_x, old_vel_y + add_vel_y)

    # If the player wants to shoot
    if pygame.K_SPACE in keys_pressed:
        last_shot = player["last_shot_time"]

        time_since_last_shot = time.time() - last_shot

        if time_since_last_shot > FIRING_RATE:
            player["last_shot_time"] = time.time()
            shot_speed = direction_from_angle(player["angle"], BULLET_SPEED)
            add_bullet(game_state, player["position"], shot_speed)



def main():
    game_state = init_gamestate()
    assets = load_assets()

    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    keys_pressed = set()


    # Initialising timer based movement. TBM ensures that things in the game
    # move at a constant speed that doesn't depend on how fast the game is running
    # in general.
    # The idea is to multiply all movement by how long the last iteration of the game loop took
    last_frame_time = time.time()

    # Instead of while running = true, we need to use gamestate
    # so that handle_events which can't access a running variable
    # can close the game
    while game_state["running"]:
        # Calculating the time the last frame took
        new_frame_time = time.time()
        delta_t = new_frame_time - last_frame_time # The time between the last frame and this frame
        last_frame_time = new_frame_time
        
        do_game_logic(game_state, delta_t)

        draw_game(game_state, assets, screen)

        handle_events(game_state, keys_pressed, delta_t)


# If the script is run directly (python3 asteroids.py) start the main function, but don't start it
# if the file is being imported
if __name__ == "__main__":
    main()

