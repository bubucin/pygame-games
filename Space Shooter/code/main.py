import pygame
from random import randint
from os.path import join
## Start Pygame ##
pygame.init()

## Display settings ##
win_width = 800
win_height = 500
screen = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Space Shooter")

## Clock ##
clock = pygame.time.Clock()

## Surfaces ##
# Player #
player_surf = pygame.image.load(join("../""images","player.png")).convert_alpha()
player_rect = player_surf.get_frect(center = ((win_width/2),(win_height/2)))
player_direction = pygame.math.Vector2(0,0)
player_speed = 300
# Star #
star_surf = pygame.image.load(join("../""images","star.png")).convert_alpha()
star_pos = [(randint(-20,780),randint(-20,480)) for i in range(20)]
# Meteor #
meteor_surf = pygame.image.load(join("../""images","meteor.png")).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = ((win_width/2),(win_height/2)))
# Laser #
laser_surf = pygame.image.load(join("../""images","laser.png")).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20,500-20))

## Loop ##
running = True
while running:
    dt = clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            player_rect.center = event.pos
    screen.fill("royalblue4")
    for pos in star_pos:
        screen.blit(star_surf,pos)
    screen.blit(meteor_surf,meteor_rect)
    screen.blit(laser_surf,laser_rect)

    # Player Movement #
    #/ Formula: rect.center += direction * speed * DeltaTime /#
    player_rect.center += player_direction*player_speed*dt
    screen.blit(player_surf,player_rect)

    # Update the frames #
    pygame.display.update()

# Quit Pygame #
pygame.quit()
