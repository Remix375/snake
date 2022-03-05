import pygame

import random

from snake.Snake import Snake
from UI.Score import Score

class Plateau:
    def __init__(self, fenetre, size=9):
        self.plateau_size = size

        self.x_window_size = fenetre.get_size()[0]
        self.y_window_size = fenetre.get_size()[1]

        #size of board
        self.board_size_x = 0.8 * self.x_window_size
        self.board_size_y = 0.8 * self.y_window_size

        #size of border of game
        self.border_x = 0.1 * self.x_window_size
        self.border_y = 0.1 * self.y_window_size

        #size of case on board
        self.size_x = self.board_size_x // size
        self.size_y = self.board_size_y // size

        

        self.position_cherry = (random.randint(0, self.plateau_size-1), random.randint(0, self.plateau_size-1))

        self.snake = Snake()

        self.can_turn = True

        self.score = Score((1,1))


    def draw(self, fenetre, tick):
        #iterate to create board
        for vertical in range(self.plateau_size):
            for horizontal in range(self.plateau_size):
                
                #get x and y position in pixels
                pos_x = self.size_x * (horizontal) + self.border_x
                pos_y = self.size_y * (vertical) + self.border_y

                #create a square
                square = pygame.Rect(pos_x, pos_y, self.size_x, self.size_y)

                #2 color grid
                if (vertical + horizontal) % 2 == 0:
                    pygame.draw.rect(fenetre, "#00fa4f", square)
                else:
                    pygame.draw.rect(fenetre, "#008c2c", square)


                #if snake on cherry:
                #grow and relocate cherry and add to score
                if self.position_cherry == self.snake.position_head():
                    #add one to score
                    self.score.add_score()
                    #grow the snake
                    self.snake.grow()

                    possible = []
                    for i in range(self.plateau_size):
                        for j in range(self.plateau_size):
                            if (i, j) not in self.snake:
                                possible.append((i, j))
                    self.position_cherry = possible[random.randint(0, len(possible)-1)]

                #red circle for the cherry just cause
                if (vertical, horizontal) == self.position_cherry:
                    pygame.draw.circle(fenetre, "red", (pos_x + self.size_x//2, pos_y + self.size_y//2), self.size_x//3)
        
        #draw snake
        self.snake.draw(fenetre, (self.size_y, self.size_x), (self.border_y, self.border_x), tick)
        #draw score
        self.score.draw(fenetre)  

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
        return self.check_if_dead()



    def check_if_dead(self):
        return self.snake.is_dead(self.plateau_size)


    def reinitialise(self):
        self.snake = Snake()
        self.can_turn = True
        self.position_cherry = (random.randint(0, self.plateau_size-1), random.randint(0, self.plateau_size-1))









