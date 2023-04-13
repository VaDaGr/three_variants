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

clickedBlock = False
clickedBlock1 = False
clickedBlock2 = False
clickedBlock3 = False
clickedBlock4 = False
clickedBlock5 = False
clickedBlock6 = False
clickedBlock7 = False
clickedBlock8 = False
clickedBlock9 = False
clickedBlock10 = False
clickedBlock11 = False
clickedBlock12 = False
clickedBlock13 = False
clickedBlock14 = False
clickedBlock15 = False
clickedBlock16 = False
clickedBlock17 = False
clickedBlock18 = False
clickedBlock19 = False
clickedBlock20 = False
clickedBlock21 = False

block1.fill(white)
block2.fill(white)
block3.fill(white)

extrablock1 = pygame.image.load('Priest.webp')
extrablock1rect = extrablock1.get_rect

extrablock2 = pygame.image.load('Vampir.webp')      
extrablock2rect = extrablock2.get_rect

extrablock3 = pygame.image.load('Rogue.webp')
extrablock3rect = extrablock3.get_rect

# z = pygame.image.load('photozero.jpg')

fes = pygame.font.Font(None, 60)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                activeBlock = 1
                clickedBlock = True
            elif event.key == pygame.K_2:
                activeBlock = 2
                clickedBlock = True
            elif event.key == pygame.K_3:
                activeBlock = 3
                clickedBlock = True
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    mainScreen.fill(purple)

    print(activeBlock)

    if clickedBlock == False:
        mainScreen.blit(block1, blockrect1)
        mainScreen.blit(block2, blockrect2)
        mainScreen.blit(block3, blockrect3)
    elif clickedBlock == True:
        if activeBlock == 1:
            mainScreen.fill(black)
            mainScreen.blit(extrablock1, extrablock1rect)
            extrablock1.x = 1000
            extrablock1.y = 500
            # sc_text = fes.render('Всё началось давным-давно', 1 , white)
            # mainScreen.blit(sc_text, (0, 0))
        if activeBlock == 2:
            mainScreen.fill(black)
            mainScreen.blit(extrablock2, extrablock2rect)
            extrablock2rect.x = 1000
            extrablock2rect.y = 500
        if activeBlock == 3:
            mainScreen.fill(black)
            mainScreen.blit(extrablock3, extrablock3rect)
            extrablock3rect.x = 1000
            extrablock3rect.y = 500


    pygame.display.flip()























































        # if clickedBlock == False:
    #     mainScreen.blit(block1, blockrect1)
    #     mainScreen.blit(block2, blockrect2)
    #     mainScreen.blit(block3, blockrect3)
    # elif clickedBlock == True and activeBlock == 1:
    #     mainScreen.fill(black)
    #     extrablock1 = pygame.image.load('Priest.webp')
    # elif clickedBlock == True and activeBlock == 2:
    #     mainScreen.fill(black)
    #     extrablock2 = pygame.image.load('Vampir.webp')  
    # elif clickedBlock == True and activeBlock == 3:
    #     mainScreen.fill(black)
    #     extrablock3 = pygame.image.load('Rogue.webp')