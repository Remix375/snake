
from snake.Snake_Part import Snake_Part



class Snake:
    def __init__(self):
        self.body = [Snake_Part((4, 4), (0, -1), True)]
        self.size = 0


    def draw(self, board, case):
        for piece in self.body:
            piece.draw(board, case)

    def position_head(self):
        return self.body[0].position

    def grow(self):
        #grow the snake by 1 in length
        #set direction and position of new element of the snake
        direction = self.body[-1].direction_end
        #position will be just behind the last current element
        position = (self.body[-1].position[0] - direction[0], self.body[-1].position[1] - direction[1])
        self.body.append(Snake_Part(position, direction))
        self.size += 1

    def turn(self, direction):
        #turn the head of the snake
        #only if direction isn't behind
        if not (self.body[0].direction_end[0] + direction[0] == 0 and self.body[0].direction_end[1] + direction[1] == 0):
            self.body[0].turn(direction)
 
    def move(self):
        #last part goes poof
        #new part one case ahead
        #having a class for each part seams useless but f*ck it maybe it will be useful
        self.body.insert(0, Snake_Part((self.body[0].position[0] + self.body[0].direction_end[0], self.body[0].position[1] + self.body[0].direction_end[1]), self.body[0].direction_end, True))
        self.body.pop()
        


    def __contains__(self, position):
        #see if the snake has an element on a square
        #usefull don't worry
        for element in self.body:
            if element.position == position:
                return True
        return False
        
