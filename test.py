
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True



circles = []

class Circle:

    def __init__(self,centered = False, color=(255,0,0),radius=10):
        
        self.radius = radius

        if centered:
            self.position = (1280/2, 720/2)
            self.color = (0,0,255)
        else:
            self.position = pygame.mouse.get_pos()
            self.color = color

    def draw(self):
        pygame.draw.circle(screen,self.color,self.position,self.radius)





circles.append(Circle(True))

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            circles.append(Circle())

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                angle = math.degree(math.atan((circles[1].position[1] - circles[0].position[1]) / (circles[1].position[0] - circles[0].position[0])))

                measurey = circles[1].position[1] - circles[0].position[1]
                measurex = circles[1].position[0] - circles[0].position[0]

                if measurey < 0:
                    if measurex > 0:
                        angle *= -1
                    else:
                        angle = 180 - angle
                else:
                    if measurex > 0:
                        angle = 360 - angle
                    else:
                        angle = 180 - angle

                # radian = angle
                # degree = math.degrees(radian)

                print(angle)
            elif event.key == pygame.K_DOWN:
                circles=[]
                circles.append(Circle(True))


       



    screen.fill("purple")

    pygame.draw.line(screen, (0,0,0), (1280/2, 0), (1280/2, 720), 3)
    pygame.draw.line(screen, (0,0,0), (0, 720/2), (1280, 720/2), 3)


    for i in circles:
        i.draw()


    

  

    pygame.display.flip()

    clock.tick(60)

pygame.quit()