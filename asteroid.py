# asteroid.py
import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        """
        Initializes an Asteroid, inheriting position and radius from CircleShape.
        """
        super().__init__(x, y, radius)
        # Note: self.velocity is inherited and needs to be set elsewhere for movement

    def draw(self, screen):
        """
        Overrides the draw method to render the asteroid as a hollow circle.
        """
        # Color: White (RGB: 255, 255, 255)
        color = (255, 255, 255)
        # Line width of 2
        line_width = 2
        
        # Use pygame.draw.circle
        pygame.draw.circle(
            surface=screen,
            color=color,
            center=(int(self.position.x), int(self.position.y)),
            radius=self.radius,
            width=line_width
        )

    def update(self, dt):
        """
        Overrides the update method to move the asteroid in a straight line.
        """
        # Move: position += velocity * dt
        self.position += self.velocity * dt