import pygame


class Snake_Part:
    def __init__(self, position, direction):

        self.position = position
        self.direction_start = direction
        self.direction_end = direction


    #drawing the part of the snake
    def draw(self, fenetre, size, border, percentage = 1, head = False):
        #size
        size_x = 0
        size_y = 0
        #if going up or down:
        #x coord will be in middle of collumn
        #y coord will be size of percentage
        #can be growing...
        if self.direction_end[1] == 0:
            size_x = 0.8 * size[1]
            size_y = percentage * size[0] + 1
        #going left or right other way around
        elif self.direction_end[0] == 0:
            size_y = 0.8 * size[0] 
            size_x = percentage * size[1] + 1

        #set basic positions
        pos_y = border[0] + (size[0] * self.position[0])
        pos_x = border[1] + (size[1] * self.position[1])

        #if the part to draw is the head of the snake
        #draw from right position to simulate movement
        #+1 at the end to avoid gap
        if head:
            if self.direction_end[0] == -1:
                pos_y = border[0] + (size[0] * (self.position[0] + 1)) - size_y + 1
            if self.direction_end[1] == -1:
                pos_x = border[1] + (size[1] * (self.position[1]+1)) - size_x + 1
        #if the part isn't the head
        #for tail
        else:
            if self.direction_end[0] == 1:
                pos_y = border[0] + (size[0] * (self.position[0]+1)) - size_y + 1
            if self.direction_end[1] == 1:
                pos_x = border[1] + (size[1] * (self.position[1]+1)) - size_x + 1

        #draw in the middle of square
        if self.direction_end[1] == 0:
            pos_x += 0.1 * size[0]                   
        elif self.direction_end[0] == 0:
            pos_y += 0.1 * size[1] 

        rectangle = pygame.Rect(pos_x, pos_y, size_x, size_y)
        pygame.draw.rect(fenetre, "black", rectangle)

    def turn(self, direction):
        self.direction_end = direction

    
    def __repr__(self):
        return str(self.position) + str(self.direction_end)
    def __str__(self):
        return str(self.position) + str(self.direction_end)