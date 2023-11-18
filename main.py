import pygame
from config import config

from sprites.player import Player
from sprites.shop import Shop
from sprites.grass_land import GrassLand

pygame.init()
pygame.display.set_caption(config.window_title)

window = pygame.display.set_mode(config.window_size)
game = True
clock = pygame.time.Clock()
fps = 60

player = Player()
shop = Shop()

grass_land = GrassLand()

while game:
    # clock.tick(fps)
    fps_check = clock.tick(fps)
    time_check = pygame.time.get_ticks()
    
    window.fill((255, 255, 255))

    # player.move((1,0), (1,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            
    # shop.toggle_shop_state()

    grass_land.animate(time_check)

    window.blit(*grass_land.get_blit())
    # window.blit(*shop.get_blit())
    pygame.display.update()