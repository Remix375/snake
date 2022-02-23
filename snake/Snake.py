
from snake.Snake_Part import Snake_Part



class Snake:
    def __init__(self):
        self.body = [Snake_Part((4, 4), (0, -1))]
        self.size = 0

    def position_head(self):
        return self.body[0].position

    def grow(self):
        #grow the snake by 1 in length
        #set direction and position of new element of the snake
        direction = self.body[-1].direction
        #position will be just behind the last current element
        position = (self.body[-1].position[0] - direction[0], self.body[-1].position[1] - direction[1])
        self.body.append(Snake_Part(position, direction))
        self.size += 1

    def turn(self, direction):
        #turn the head of the snake
        #body should follow if I can code
        #only if direction isn't behind
        if not (self.body[0].direction[0] + direction[0] == 0 and self.body[0].direction[1] + direction[1] == 0):
            self.body[0].turn(direction)
 
    def move(self):
        #each part takes properties of part before it
        #having a class for each part seams useless but f*ck it maybe it will be useful
        for part in range(len(self.body)-1, 0, -1):
            self.body[part].position = self.body[part-1].position
            self.body[part].direction = self.body[part-1].direction
        self.body[0].update_position()

    def __contains__(self, position):
        #see if the snake has an element on a square
        #usefull don't worry
        for element in self.body:
            if element.position == position:
                return True
        return False
        
