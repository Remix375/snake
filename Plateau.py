import pygame

from snake.Snake import Snake


class Plateau:
    def __init__(self, fenetre, size=10):
        #directions: (0, -1) -> left | (0, 1) -> right | (1, 0) -> down | (-1, 0) -> up
        #start facing left
        self.direction = (-1, 0)

        self.plateau_size = size

        self.x_window_size = fenetre.get_size()[0]
        self.y_window_size = fenetre.get_size()[1]

        #size of a case on board
        self.size_x = (0.8 * self.x_window_size) // size
        self.size_y = (0.8 * self.y_window_size) // size


        self.snake = Snake()


    def draw(self, fenetre):
        for vertical in range(self.plateau_size):
            for horizontal in range(self.plateau_size):

                pos_x = self.size_x * (horizontal + 1)
                pos_y = self.size_y * (vertical + 1)


                square = pygame.Rect(pos_x, pos_y, self.size_x, self.size_y)

                if (vertical + horizontal) % 2 == 0:
                    pygame.draw.rect(fenetre, "#00fa4f", square)
                else:
                    pygame.draw.rect(fenetre, "#008c2c", square)

                for placement in self.snake.body:
                    if (vertical, horizontal) == placement[0]:
                        pygame.draw.circle(fenetre, "black", (pos_x + self.size_x//2, pos_y + self.size_y//2), self.size_x//2)

    def change_direction(self, direction):
        self.snake.turn(direction)

    def move(self, fenetre):
        self.snake.move()

