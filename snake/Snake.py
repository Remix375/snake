


class Snake:
    def __init__(self):
        self.body = [[(4, 4), (0, -1)]]


    def grow(self):
        self.body.append(self.body[-1])

    def turn(self, direction):
        self.body[0][1] = direction
 
    def move(self):
        self.body[0] = [(self.body[0][0][0] + self.body[0][1][0], self.body[0][0][1] + self.body[0][1][1]), self.body[0][1]]
        print(self.body)
        for k in range(1, len(self.body)-1):
            self.body[k] = self.body[k-1]
        
