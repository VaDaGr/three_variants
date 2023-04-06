import pygame, sys
pygame.init()

WIDTH = 1920
HEIGHT = 1080
black = 0, 0, 0
white = 255, 255, 255

mainScreen = pygame.display.set_mode(((WIDTH, HEIGHT)),pygame.FULLSCREEN)

activeBlock = 0

block1 = pygame.image.load('Priest.webp')    
block2d = pygame.image.load('Vampir.webp')    
block3d = pygame.image.load('Rogue.webp')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
            sys.exit()

    if event.key == pygame.K_1:
        activeBlock = 1
    elif event.key == pygame.K_2:
        activeBlock = 2  
    elif event.key == pygame.K_3:
        activeBlock = 3    

    
    if activeBlock == 1:
        mainScreen.fill(black)
        block1 = pygame.image.load('Priest.webp')      
    if activeBlock == 2:
        mainScreen.fill(black)
        block2d = pygame.image.load('Vampir.webp')      
    if activeBlock == 3:
        mainScreen.fill(black)
        block3d = pygame.image.load('Rogue.webp')

    mainScreen.fill(black)

    pygame.draw.rect(mainScreen, white, (240, 270, 640, 810))

    pygame.display.flip()