

def init(py, scr):
    global pygame,screen

    pygame = py
    screen = scr





class Circle:
    radius = 10
    def __init__(self,color=(255,0,0),radius=10):
        self.color = color
        self.radius = radius
        self.position = pygame.mouse.get_pos()

    def draw(self):
        pygame.draw.circle(screen,self.color,self.position,self.radius)




