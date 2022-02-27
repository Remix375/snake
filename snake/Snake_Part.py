import pygame


class Snake_Part:
    def __init__(self, position, direction):

        self.position = position
        self.direction_start = direction
        self.direction_end = direction



    def draw(self, fenetre, size, border, percentage = 1, head = False):
        print(size)
        print(percentage)
        pos_y = border[0] + (size[0] * self.position[0])
        pos_x = border[1] + (size[1] * self.position[1])
        size_x = 0
        size_y = 0
        if self.direction_end[1] == 0:
            size_x = 0.8 * size[1]
            size_y = percentage * size[0]
        elif self.direction_end[0] == 0:
            size_y = 0.8 * size[0]
            size_x = percentage * size[1]

        rectangle = pygame.Rect(pos_x, pos_y, size_x, size_y)
        pygame.draw.rect(fenetre, "black", rectangle)

    def turn(self, direction):
        self.direction_end = direction

    
    def __repr__(self):
        return str(self.position) + str(self.direction_end)
    def __str__(self):
        return str(self.position) + str(self.direction_end)