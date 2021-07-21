import pygame
import random

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Rock Paper Scissors')
clock = pygame.time.Clock()
choice=['rock','paper','scissor']
background = pygame.image.load('background.png')
while True:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()
