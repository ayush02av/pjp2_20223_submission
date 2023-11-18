import pygame

class Base:
    MOVEMENT = 10
    
    def __init__(
        self,
        path: str,
        position: tuple,
        size: tuple,
        speed: int = 10,
        animation_frames: list = [],
        animation_frame_cooldown: int = 200
    ):
        self.size = size
        self.speed = speed

        self.update_visual(path)
        self.position = self.sprite.get_rect()
        self.position.center = position

        self.last_tick = 0
        self.animation_frame = 0
        self.animation_frames = animation_frames
        self.animation_frame_cooldown = animation_frame_cooldown
        
    def animate(
        self,
        tick: int
    ):
        if tick - self.last_tick < self.animation_frame_cooldown:
            return
        
        self.last_tick = tick
    
        self.animation_frame += 1
        if self.animation_frame >= len(self.animation_frames):
            self.animation_frame = 0
        
        self.update_visual(self.animation_frames[self.animation_frame])
        
    def move(
        self,
        direction: list
    ):
        if direction[0] != 0 and direction[1] != 0:
            direction = (direction[0], 0)

        self.position.x += int(direction[0] * self.speed / self.MOVEMENT)
        self.position.y += int(direction[1] * self.speed / self.MOVEMENT)
    
    def update_visual(
        self,
        path: str
    ):
        self.sprite = pygame.transform.scale(pygame.image.load(f"assets/{path}"), self.size)
    
    def get_visual(self):
        return self.sprite
    
    def get_rect(self):
        return self.position

    def get_blit(self):
        return (self.get_visual(), self.get_rect())