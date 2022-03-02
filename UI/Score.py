import pygame
pygame.init()

class Score:

    def __init__(self, pos, size=0) -> None:
        self.pos = pos

        self.size = size

        self.score = 1

        self.font = pygame.font.SysFont("comicsans", 25)

    def draw(self, fenetre):
        text = self.font.render("Score: " + str(self.score), True, (0,0,0))
        fenetre.blit(text, (self.pos[1], self.pos[0]))



    def add_score(self):
        self.score += 1

