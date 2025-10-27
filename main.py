import pygame
from constants import *

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Age of Dragons: Asteroids")

    # Game Loop (Infinite while loop)
    while True:
        # Step 1: Check for player inputs (including quitting)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit the function (and thus the game loop) if the user closes the window
                return

        # Step 2: Update the game world (Placeholder for now)
        # ... your game logic updates will go here ...

        # Step 3: Draw the game to the screen
        
        # Fill the screen with a solid "black" color (RGB: 0, 0, 0)
        screen.fill((0, 0, 0)) 
        
        # Use pygame's display.flip() method to refresh the screen (must be called last)
        pygame.display.flip()
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    # Expected output when running main.py:
    # Starting Asteroids!
    # Screen width: 1280
    # Screen height: 720

if __name__ == "__main__":
    main()
