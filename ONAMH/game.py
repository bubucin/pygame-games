import pygame
import random
from os.path import join
from time import sleep

pygame.init()

clock = pygame.Clock()

WIN_HEIGHT = 600 
WIN_LENGHT = 800

screen = pygame.display.set_mode((WIN_LENGHT,WIN_HEIGHT))
pygame.display.set_caption("One Night at my House")

class Cameras:
    def __init__(self, camera_number,):
        pass

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(60) / 1000

    pygame.display.flip()