
import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

record = False


screen.fill("purple")



class Circle:

    def __init__(self,color=(255,0,0),radius=10):
        self.color = color
        self.radius = radius
        self.position = pygame.mouse.get_pos()

    def draw(self):
        pygame.draw.circle(screen,self.color,self.position,self.radius)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            record = True
        elif event.type == pygame.MOUSEBUTTONUP:
            record = False


    if record:
        # pos = pygame.mouse.get_pos()
        # print(pos)

        Circle().draw()

    
    # pygame.draw.circle(screen,(255,0,0),(300,300),20)

  

    pygame.display.flip()

    clock.tick(60)

pygame.quit()