import pygame

class Base:
    MOVEMENT = 10
    
    def __init__(
        self,
        path: str,
        position: str,
        speed: int = 10
    ):
        self.update_visual(path)
        self.speed = speed

        self.position = self.sprite.get_rect()
        self.position.center = position
        
    def move(
        self,
        direction: list,
        magnitude: list
    ):
        self.position.x += direction[0] * magnitude[0] * self.speed / self.MOVEMENT
        self.position.y += direction[1] * magnitude[1] * self.speed / self.MOVEMENT
    
    def update_visual(
        self,
        path: str
    ):
        self.sprite = pygame.image.load(f"assets/{path}")
    
    def get_visual(self):
        return self.sprite
    
    def get_rect(self):
        return self.position

    def get_blit(self):
        return (self.get_visual(), self.get_rect())