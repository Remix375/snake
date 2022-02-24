import pygame
pygame.init()

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.font = font = pygame.font.SysFont("comicsans", 60)

    def draw(self,fenetre,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(fenetre, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(fenetre, self.color, (self.x,self.y,self.width,self.height),0)
        
        #writing text in button
        if self.text != '':
            text = self.font.render(self.text, True, (0,0,0))
            fenetre.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        #checks to see if the position is on the button
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False