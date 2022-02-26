import pygame


class Snake_Part:
    def __init__(self, position, direction, head = False):

        self.position = position
        self.direction_start = direction
        self.direction_end = direction


        self.head = head

        self.percentage = 0


    def draw(self, fenetre, pos):
        fenetre.blit

    def update_position(self):
        #udate position
        #basically only usefull for the head
        self.position = (self.position[0] + self.direction_end[0], self.position[1] + self.direction_end[1])

    def turn(self, direction):
        self.direction_end = direction

    
    def __repr__(self):
        return str(self.position) + str(self.direction_end)
    def __str__(self):
        return str(self.position) + str(self.direction_end)