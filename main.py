import pygame
from config import config

from sprites.grass_land import GrassLand
from sprites.barren_land import BarrenLand
from sprites.player import Player

pygame.init()
pygame.display.set_caption(config.window_title)

window = pygame.display.set_mode(config.window_size)
game = True
clock = pygame.time.Clock()
fps = 60

farm_start = (20, 310)
land_size = (41, 43)
rows_of_farm = 8
cols_of_farm = 5

farm = [
    [
        BarrenLand(
            (
                farm_start[0] + (land_size[0] * i),
                farm_start[1] + (land_size[1] * j)
            )
        )
        for j in range(cols_of_farm)
    ]
    for i in range(rows_of_farm)
]

player = Player()

while game:
    fps_check = clock.tick(fps)
    time_check = pygame.time.get_ticks()
    
    window.fill((255, 255, 255))

    for row in farm:
        for land in row:
            # land.animate(time_check)
            window.blit(*land.get_blit())
        

    keys = pygame.key.get_pressed()
    player_movement_direction = [0, 0]

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_movement_direction[0] = -1

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_movement_direction[0] = 1
    
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_movement_direction[1] = -1
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_movement_direction[1] = 1
    
    player.animate(time_check)
    if player_movement_direction != [0, 0]:
        player.move(tuple(player_movement_direction))
    
    window.blit(*player.get_blit())
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False