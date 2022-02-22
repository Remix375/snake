import pygame, sys
import time


from Plateau import Plateau


hauteur, largeur = 1000, 1000
fenetre = pygame.display.set_mode((hauteur, largeur))
background = (100, 135, 110)

clock = pygame.time.Clock()
last_tick = 0

board = Plateau(fenetre)

continuer = True


while continuer:
    fenetre.fill(background)
    board.draw(fenetre)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                board.change_direction((0, -1))

            if event.key == pygame.K_RIGHT:
                board.change_direction((0, 1))

            if event.key == pygame.K_UP:
                board.change_direction((-1, 0))

            if event.key == pygame.K_DOWN:
                board.change_direction((1, 0))

            if event.key == pygame.K_SPACE:
                print("DFD")
                board.grow()

    if pygame.time.get_ticks() - last_tick > 500:
        board.move(fenetre)
        last_tick = pygame.time.get_ticks()

    pygame.display.update()
    clock.tick(60)


pygame.display.quit()

sys.exit()









#⊂(◉‿◉)つ