


class Snake_Part:
    def __init__(self, position, direction):

        self.position = position
        self.direction = direction


    def update_position(self):
        self.position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])

    def turn(self, direction):
        self.direction = direction

    def __str__(self):
        return str(self.position) + str(self.direction)