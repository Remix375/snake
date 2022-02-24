import pygame


class Snake_Part:
    def __init__(self, position, direction, head = False):

        self.position = position
        self.direction = direction

        self.head = head

        self.image = pygame.image.load("./snake/images/body_straight.png")


    def draw(self, fenetre, pos):
        fenetre.blit

    def update_position(self):
        #udate position
        #basically only usefull for the head
        self.position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])

    def turn(self, direction):
        self.direction = direction

    
    def __repr__(self):
        return str(self.position) + str(self.direction)
    def __str__(self):
        return str(self.position) + str(self.direction)