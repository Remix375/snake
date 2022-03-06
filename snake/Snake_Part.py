import pygame


class Snake_Part:
    def __init__(self, position, direction):

        self.position = position
        self.direction_start = direction
        self.direction_end = direction


    #drawing the part of the snake
    def draw(self, fenetre, size, border, percentage = 1, tail = False):

        if tail:
            percentage = 1-percentage
        #setting percentages of start and end
        #we draw them seperately for turns
        percentage_start, percentage_end = 0, 0
        if percentage >= 0.5:
            percentage_start = 1
            percentage_end = (percentage - 0.5) * 2
        else:
            percentage_start = percentage * 2
            percentage_end = 0


        if tail:
            percentage_end, percentage_start = percentage_start, percentage_end


        #draw first part of snake
        #positions and sizes of part of snake to draw
        pos_x_start = 0
        pos_y_start = 0
        size_x_start = 0
        size_y_start = 0

        #going down
        if self.direction_start == (1, 0):
            pos_y_start = border[0] + self.position[0] * size[0]
            pos_x_start = border[1] + self.position[1] * size[1] + 0.1 * size[1]

            size_y_start = percentage_start * (size[0] // 2) + 1
            size_x_start = 0.8 * size[1]

            if tail:
                pos_y_start += (1 - percentage_start) * (size[0]//2)


        #going right
        if self.direction_start == (0, 1):
            pos_y_start = border[0] + self.position[0] * size[0] + 0.1 * size[0]
            pos_x_start = border[1] + self.position[1] * size[1]

            size_y_start = 0.8 * size[0]
            size_x_start = percentage_start * (size[1] // 2) + 1

            if tail:
                pos_x_start += (1 - percentage_start) * (size[1]//2)


        #going up
        if self.direction_start == (-1, 0):
            pos_y_start = border[0] + self.position[0] * size[0] + (2 - percentage_start) * (size[0] // 2)
            pos_x_start = border[1] + self.position[1] * size[1] + 0.1 * size[1]

            size_y_start = percentage_start * (size[0] // 2) + 1
            size_x_start = 0.8 * size[1]

            if tail:
                pos_y_start -= (1 - percentage_start) * (size[0]//2)

        #going left
        if self.direction_start == (0, -1):
            pos_y_start = border[0] + self.position[0] * size[0] + 0.1 * size[0]
            pos_x_start = border[1] + self.position[1] * size[1] + (1 + (1 - percentage_start)) * (size[1] // 2)

            size_y_start = 0.8 * size[0]
            size_x_start = percentage_start * (size[1] // 2) + 1

            if tail:
                pos_x_start -= (1 - percentage_start) * (size[1]//2)
            









        #draw second part of snake
        #positions and sizes of part of snake to draw
        pos_x_end = 0
        pos_y_end = 0
        size_x_end = 0
        size_y_end = 0

        #going down
        if self.direction_end == (1, 0):
            pos_y_end = border[0] + self.position[0] * size[0] + size[0] // 2
            pos_x_end = border[1] + self.position[1] * size[1] + 0.1 * size[1]

            size_y_end = percentage_end * (size[0] // 2) + 1
            size_x_end = 0.8 * size[1]

            if tail:
                pos_y_end += (1-percentage_end) * (size[0] // 2)

        #going right
        if self.direction_end == (0, 1):
            pos_y_end = border[0] + self.position[0] * size[0] + 0.1 * size[0]
            pos_x_end = border[1] + self.position[1] * size[1] + size[1] // 2

            size_y_end = 0.8 * size[0]
            size_x_end = percentage_end * (size[1] // 2) + 1

            if tail:
                pos_x_end += (1-percentage_end) * (size[1] // 2)


        #going up
        if self.direction_end == (-1, 0):
            pos_y_end = border[0] + self.position[0] * size[0] + (1 - percentage_end) * (size[0] // 2)
            pos_x_end = border[1] + self.position[1] * size[1] + 0.1 * size[1]

            size_y_end = percentage_end * (size[0] // 2) + 1
            size_x_end = 0.8 * size[1]

            if tail:
                pos_y_end -= (1-percentage_end) * size[0] // 2



        #going left
        if self.direction_end == (0, -1):
            pos_y_end = border[0] + self.position[0] * size[0] + 0.1 * size[0]
            pos_x_end = border[1] + self.position[1] * size[1] + (1 - percentage_end) * (size[1] // 2)

            size_y_end = 0.8 * size[0]
            size_x_end = percentage_end * (size[1] // 2) + 1

            if tail:
                pos_x_end -= (1-percentage_end) * size[1] // 2

        if not (tail and percentage < 0.5):
            #draw start
            rectangle_start = pygame.Rect(pos_x_start, pos_y_start, size_x_start, size_y_start)
            pygame.draw.rect(fenetre, "black", rectangle_start)

        if not (not tail and percentage < 0.5):
            #draw end if exists
            rectangle_end = pygame.Rect(pos_x_end, pos_y_end, size_x_end, size_y_end)
            pygame.draw.rect(fenetre, "black", rectangle_end)


























        """
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
        """









        """
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
        """



    def turn(self, direction):
        self.direction_end = direction

    
    def __repr__(self):
        return str(self.position) + str(self.direction_end)
    def __str__(self):
        return str(self.position) + str(self.direction_end)