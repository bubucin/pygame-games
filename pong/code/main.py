import pygame
from os.path import join

pygame.init()

clock = pygame.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Emoji Pong")

pong_surf = pygame.image.load(join("../""assets/""pong_thing.png"))
pong_rect = pong_surf.get_frect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/1.2))

ball_surf = pygame.image.load(join("../""assets/""ball.png"))
ball_rect = ball_surf.get_frect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
ball_direction = pygame.Vector2(1,1)
ball_speed = 250

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(60) / 1000

    screen.fill("gray20")
    screen.blit(pong_surf,pong_rect)
    screen.blit(ball_surf,ball_rect)
    # Movement #
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        pong_rect.x -= 300*dt
    elif key[pygame.K_RIGHT]:
        pong_rect.x += 300*dt
    elif pong_rect.x == 600:
        pong_rect.x += 300*dt
    elif pong_rect.x == 0:
        pong_rect.x -= 300*dt

    # Ball Movement #
    ball_rect.center+=ball_direction*ball_speed*dt
    # Ball Bounce #
    if ball_rect.bottom >= SCREEN_HEIGHT:
        ball_rect.bottom = SCREEN_HEIGHT
        ball_direction.y *= -1
    elif ball_rect.top <= 0:
        ball_rect.top = 0
        ball_direction.y *= -1
    elif ball_rect.right >= SCREEN_WIDTH:
        ball_rect.right = SCREEN_WIDTH
        ball_direction.x *= -1
    elif ball_rect.left <= 0:
        ball_rect.left = 0
        ball_direction.x *= -1
    pygame.display.update()
pygame.quit()
