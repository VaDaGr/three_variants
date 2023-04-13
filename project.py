import pygame, sys
pygame.init()

WIDTH = 1920
HEIGHT = 1080
black = 0, 0, 0
white = 255, 255, 255
purple = (136, 0, 255)

mainScreen = pygame.display.set_mode(((WIDTH, HEIGHT)),pygame.FULLSCREEN)

activeBlock = 0

block1 = pygame.Surface((440, 840))
block2 = pygame.Surface((440, 840))
block3 = pygame.Surface((440, 840))

blockrect1 = block1.get_rect()
blockrect1.x = 50
blockrect1.y = 120
blockrect2 = block2.get_rect()
blockrect2.x = 690
blockrect2.y = 120
blockrect3 = block3.get_rect()
blockrect3.x = 1330
blockrect3.y = 120

# block1.fill(black)
# block2.fill(black)
# block3.fill(black)

block1.fill(white)
block2.fill(white)
block3.fill(white)

z = pygame.image.load('photozero.jpg')

fes = pygame.font.Font(None, 60)
# block1 = pygame.image.load('Priest.webp')
# block2 = pygame.image.load('Vampir.webp')      
# block3 = pygame.image.load('Rogue.webp')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                activeBlock = 1
            elif event.key == pygame.K_2:
                activeBlock = 2
            elif event.key == pygame.K_3:
                activeBlock = 3
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    mainScreen.fill(purple)

    if activeBlock == 1:
        mainScreen.fill(black)
        block1 = pygame.image.load('Priest.webp')
        sc_text = fes.render('Всё началось давным-давно', 1 , white)
        mainScreen.blit(sc_text, (0, 0))
    if activeBlock == 2:
        mainScreen.fill(black)
        block2 = pygame.image.load('Vampir.webp')      
    if activeBlock == 3:
        mainScreen.fill(black)
        block3 = pygame.image.load('Rogue.webp')

    mainScreen.blit(block1, blockrect1)
    mainScreen.blit(block2, blockrect2)
    mainScreen.blit(block3, blockrect3)
    pygame.display.flip()