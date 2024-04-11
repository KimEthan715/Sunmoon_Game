import pygame
import sys

pygame.init()

background = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("test1")

play = True
while play:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            play = False



pygame.quit()

