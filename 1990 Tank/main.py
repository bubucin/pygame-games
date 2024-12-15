import pygame
from os.path import join

pygame.init()

WIN_HEIGHT = 600
WIN_LENGHT = 800

screen = pygame.display.set_mode((WIN_LENGHT,WIN_HEIGHT))
pygame.display.set_caption("1990 Tank")
clock = pygame.time.Clock()

player_surf = pygame.image.load(join("assets","player_tank0.png")).convert_alpha()
player_rect = player_surf.get_frect(center = ((WIN_LENGHT/2),(WIN_HEIGHT/2)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(60) / 1000

    screen.fill("gray20")
    screen.blit(player_surf,player_rect)

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player_rect.y -= 300 * dt
    if key[pygame.K_s]:
        player_rect.y += 300 * dt
    if key[pygame.K_a]:
        player_rect.x -= 300 * dt
    if key[pygame.K_d]:
        player_rect.x += 300 * dt


    pygame.display.update()
