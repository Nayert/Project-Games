import pygame 

#intialise the pygame
pygame.init()

screen = pygame.display.set_mode((800,600)) # length,width
running = True

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("testing stuff/Space invaders/ufo.png")
pygame.display.set_icon(icon)

while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False



    screen.fill((123,234,255)) #RGB#
    pygame.display.update()
