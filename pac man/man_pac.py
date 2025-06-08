import pygame
from pygame.locals import *

pygame.init()
SCREEN_WIDTH = 224*2.7
SCREEN_HEIGHT = 288*2.7

pt=0
pac_x=0
pac_y=0
value=0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pac_man= [  pygame.image.load('pac man/data/pac_man1.svg'),
            pygame.image.load('pac man/data/pac_man2.svg'),
            pygame.image.load('pac man/data/pac_man3.svg')
         ]

run = True

while run:


    clock.tick(6)
    print(value)

    if value >=len(pac_man):
        value=0

    pac_image = pac_man[value]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(pac_image,(pac_x,pac_y))
    print(pac_image)

    pygame.display.update()
    screen.fill((0,0,0))
    value += 1
pygame.quit()