import pygame, sys
import time


from Plateau import Plateau
from Menu.Button import Button

hauteur, largeur = 1000, 1000
fenetre = pygame.display.set_mode((hauteur, largeur))
background = (100, 135, 110)

clock = pygame.time.Clock()
last_tick = 0


tick_time = 100
board = Plateau(fenetre)

continuer = True

Play_Button = Button("blue", fenetre, "play")
playing = False



while continuer:
    fenetre.fill(background)

    if playing:
        board.draw(fenetre, (pygame.time.get_ticks() - last_tick) / tick_time)
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
                    board.grow()

                    
        if pygame.time.get_ticks() - last_tick > tick_time:
            playing = board.move(fenetre)
            last_tick = pygame.time.get_ticks()
        if not playing:
            board.reinitialise()



    else:
        Play_Button.draw(fenetre)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_Button.isOver(pos):
                    playing = True
            
        


    pygame.display.update()
    clock.tick(100)


pygame.display.quit()

sys.exit()









#⊂(◉‿◉)つ