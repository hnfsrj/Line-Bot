
import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True








class Circle:

    def __init__(self,side,color=(255,0,0),radius=20):
        self.color = color
        self.radius = radius
        self.position = [1280/2, 720/2]
        self.side = side

    def draw(self):
        pygame.draw.circle(screen,self.color,self.position,self.radius)





right_wheel = Circle(1)
left_wheel = Circle(0)

while running:

    screen.fill("purple")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
    
    circle.position[1] -= 1
    circle.draw()

    
    # pygame.draw.circle(screen,(255,0,0),((1280/2, 720/2)),20)

    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()