import pygame
from player import Player
from constants import *

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Age of Dragons: Asteroids")

    # --- Instantiate Player ---
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    # --------------------------

    clock = pygame.time.Clock()
    # Initialize the delta time (dt) variable
    dt = 0

    # Game Loop (Infinite while loop)
    while True:
        # Step 1: Check for player inputs (including quitting)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit the function (and thus the game loop) if the user closes the window
                return

        # Step 2: Update the game world (dt will be used here later)
        # ... your game logic updates will go here ...
        # print(f"Delta Time: {dt:.4f} seconds") # Uncomment to see dt value

        # Step 3: Draw the game to the screen
        
        # Fill the screen with a solid "black" color (RGB: 0, 0, 0)
        screen.fill((0, 0, 0)) 
        
        # Refresh the screen
        pygame.display.flip()

        # --- FPS Control Implementation ---
        # .tick(60) pauses the loop to restrict the FPS to a max of 60.
        # It returns the time passed since the last call (in milliseconds).
        # We divide by 1000 to convert milliseconds to seconds and save it to dt.
        dt = clock.tick(60) / 1000
        # ----------------------------------

if __name__ == "__main__":
    main()
