
from snake.Snake_Part import Snake_Part



class Snake:
    def __init__(self):
        self.body = [Snake_Part((4, 4), (0, -1))]


    def grow(self):
        direction = self.body[-1].direction
        position = (self.body[-1].position[0] - direction[0], self.body[-1].position[1] - direction[1])
        self.body.append(Snake_Part(position, direction))
        print(self.body)

    def turn(self, direction):
        self.body[0].turn(direction)
 
    def move(self):
        
        for part in range(len(self.body)-1, 0, -1):
            self.body[part].position = self.body[part-1].position
            self.body[part].direction = self.body[part-1].direction
        self.body[0].update_position()

    def __contains__(self, position):
        for element in self.body:
            if element.position == position:
                return True
        return False
        
