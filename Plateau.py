import pygame

import random

from snake.Snake import Snake


class Plateau:
    def __init__(self, fenetre, size=9):
        #directions: (0, -1) -> left | (0, 1) -> right | (1, 0) -> down | (-1, 0) -> up
        #start facing left
        self.direction = (-1, 0)

        self.plateau_size = size

        self.x_window_size = fenetre.get_size()[0]
        self.y_window_size = fenetre.get_size()[1]

        #size of a case on board
        self.size_x = (0.8 * self.x_window_size) // size
        self.size_y = (0.8 * self.y_window_size) // size


        self.position_cherry = (random.randint(0, self.plateau_size-1), random.randint(0, self.plateau_size-1))

        self.snake = Snake()

        self.can_turn = True


    def draw(self, fenetre):
        #iterate to create board
        for vertical in range(self.plateau_size):
            for horizontal in range(self.plateau_size):
                
                #get x and y position in pixels
                pos_x = self.size_x * (horizontal + 1)
                pos_y = self.size_y * (vertical + 1)

                #create a square
                square = pygame.Rect(pos_x, pos_y, self.size_x, self.size_y)

                #2 color grid
                if (vertical + horizontal) % 2 == 0:
                    pygame.draw.rect(fenetre, "#00fa4f", square)
                else:
                    pygame.draw.rect(fenetre, "#008c2c", square)

                #if snake on the case: draw a dot
                #will change no worries
                if (vertical, horizontal) in self.snake:
                    pygame.draw.circle(fenetre, "black", (pos_x + self.size_x//2, pos_y + self.size_y//2), self.size_x//2)

                #if snake on cherry:
                #grow and relocate cherry
                if self.position_cherry == self.snake.position_head():
                    self.position_cherry = (random.randint(0, self.plateau_size-1), random.randint(0, self.plateau_size-1))
                    self.snake.grow()

                #red circle for the cherry just cause
                if (vertical, horizontal) == self.position_cherry:
                    pygame.draw.circle(fenetre, "red", (pos_x + self.size_x//2, pos_y + self.size_y//2), self.size_x//3)

                

    #the snake turns
    def change_direction(self, direction):
        #only change one time of direction until the snake moves
        if self.can_turn:
            self.snake.turn(direction)
        self.can_turn = False

    #the snake moves
    def move(self, fenetre):
        self.snake.move()
        self.can_turn = True









