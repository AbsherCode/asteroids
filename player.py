import pygame
from constants import PLAYER_RADIUS # Assuming you will import constants here
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        """
        Initializes the Player ship, inheriting from CircleShape for the hitbox.
        """
        # Call the parent class's constructor, passing in PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        
        # Create a field called rotation, initialized to 0
        self.rotation = 0

    def triangle(self):
        """
        Calculates the three points for the triangle representing the ship model.
        """
        # Create a vector pointing forward (up/positive y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # Create a vector pointing right, scaled down
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        # Point A (Nose): Center + forward * radius
        a = self.position + forward * self.radius
        
        # Point B (Left Wing): Center - forward * radius - right
        b = self.position - forward * self.radius - right
        
        # Point C (Right Wing): Center - forward * radius + right
        c = self.position - forward * self.radius + right
        
        return [a, b, c]

    def draw(self, screen):
        """
        Overrides the CircleShape draw method to draw the triangle model.
        """
        # Color: White (RGB: 255, 255, 255)
        color = (255, 255, 255) 
        
        # Line width of 2
        line_width = 2
        
        # Draw the triangle polygon
        pygame.draw.polygon(screen, color, self.triangle(), line_width)