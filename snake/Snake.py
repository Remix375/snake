
from snake.Snake_Part import Snake_Part



class Snake:
    def __init__(self):
        self.body = [Snake_Part((4, 4), (0, -1))]


    def grow(self):
        self.body.append(self.body[-1])

    def turn(self, direction):
        self.body[0].turn(direction)
 
    def move(self):
        self.body[0].update_position()

        for part in range(1, len(self.body)-1):
            self.body[part] = self.body[part-1]

    def __contains__(self, position):
        for element in self.body:
            if element.position == position:
                return True
        return False
        
