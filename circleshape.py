import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, other_shape):
        """
        Checks for collision between this CircleShape and another CircleShape.

        Collision occurs if distance <= r1 + r2.
        """
        # Calculate the distance between the two center points (pygame.Vector2 method)
        distance = self.position.distance_to(other_shape.position)
        
        # Calculate the sum of the radii
        min_distance = self.radius + other_shape.radius
        
        # Check for collision (including touching edges)
        return distance <= min_distance

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass