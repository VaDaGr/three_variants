import pygame, sys
pygame.init()

WIDTH = 1920
HEIGHT = 1080
black = 0, 0, 0

mainScreen = pygame.display.set_mode(((WIDTH, HEIGHT)),pygame.FULLSCREEN)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка: ", event.button)
        

    mainScreen.fill(black)

    pygame.display.flip()
