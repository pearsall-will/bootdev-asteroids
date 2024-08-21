import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        '''Sub class must override'''
        raise NotImplementedError('''Draw not implemented in subclas''')

    def update(self, dt):
        '''Sub class must override'''
        raise NotImplementedError('''Update not implemented in subclass.''')

    def collided(self, circle):
        if not isinstance(self.position,pygame.Vector2) or not isinstance(circle.position,pygame.Vector2):
            return False
        dist = self.position.distance_to(circle.position)
        rr = self.radius + circle.radius
        return dist <= rr
