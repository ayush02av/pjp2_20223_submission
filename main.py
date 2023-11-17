import pygame
from config import config
from sprites.player import Player

pygame.init()
pygame.display.set_caption(config.window_title)

window = pygame.display.set_mode(config.window_size)
game = True
clock = pygame.time.Clock()
fps = 60

player = Player()

# fps_check = clock.tick(fps) / 1000.0
while game:
    clock.tick(fps)
    window.fill((255, 255, 255))
    
    player.move((1,0), (1,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(*player.get_blit())
    pygame.display.update()