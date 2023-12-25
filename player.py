import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 63))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction = 1
        elif keys[pygame.K_LEFT]:
            self.direction = -1
        else:
            self.direction = 0
            
    def update(self):
        self.get_input()
        self.rect.x += self.direction * self.speed