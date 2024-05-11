
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True




bots = []


class Rod:
    def __init__(self):
        self.x,self.y = pygame.mouse.get_pos()

        self.length = 60
        self.radius = self.length/2

        self.barx1 = self.x-self.radius
        self.bary1 = self.y

        self.barx2 = self.x+self.radius
        self.bary2 = self.y

        self.speed = 1
        self.degree = 0

    def draw_rod(self):
        pygame.draw.line(screen, (255,255,255), (self.barx1,self.bary1), (self.barx2,self.bary2),5)

    


    





class Tires(Rod):

    def __init__(self):
        super().__init__()

        self.tire_size = 10


    def draw_tire(self):
        pygame.draw.circle(screen,(255,0,0),(self.barx1,self.bary1),self.tire_size)
        pygame.draw.circle(screen,(255,0,0),(self.barx2,self.bary2),self.tire_size)






class Robot(Tires):
    
    def draw(self, steer = 0):
        self.steering(steer)

        self.draw_rod()
        self.draw_tire()


    def steering(self, steer):

        if self.degree == -359 or self.degree == 359:
            self.degree = 0



        if steer == 1:
            self.degree += 1

            angle = math.radians(self.degree + 180)

            change_x = self.length * math.cos(angle)
            change_y = self.length * math.sin(angle)

            self.barx1 = self.barx2+change_x
            self.bary1 = self.bary2+change_y

        elif steer == -1:
            self.degree -= 1

            angle = math.radians(self.degree)
            
            change_x = self.length * math.cos(angle)
            change_y = self.length * math.sin(angle)

            self.barx2 = self.barx1+change_x
            self.bary2 = self.bary1+change_y

        else:
            angle = math.radians(-1*self.degree + 90)

            add_x = self.speed * math.cos(angle)
            add_y = self.speed * math.sin(angle)

            self.barx1 += add_x
            self.bary1 -= add_y

            self.barx2 += add_x
            self.bary2 -= add_y
        





rotate = 0
    

while running:

    screen.fill("purple")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            bots.append(Robot())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rotate = -1
            elif event.key == pygame.K_RIGHT:
                rotate = 1
            elif event.key == pygame.K_UP:
                rotate = 0
        
    

    for i in bots:
        i.draw(rotate)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()