
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True




rods = []


class Rod:
    def __init__(self):
        x,y = pygame.mouse.get_pos()

        self.length = 60

        self.x = x
        self.y = y

        self.barx1 = self.x-(self.length/2)
        self.bary1 = self.y

        self.barx2 = self.x+(self.length/2)
        self.bary2 = self.y

        self.left_wheel_x = self.x-(self.length/2)
        self.left_wheel_y = self.y

        self.right_wheel_x = self.x+(self.length/2)
        self.right_wheel_y = self.y

        self.radius = self.length/2
        self.direction = 1

        self.speed = 1
        self.degree = 0

    def draw_rod(self,bx1,by1,bx2,by2):
        pygame.draw.line(screen, (255,255,255), (bx1,by1), (bx2,by2),5)

    def draw_tire(self,lx,ly,rx,ry):
        pygame.draw.circle(screen,(255,0,0),(lx,ly),10)
        pygame.draw.circle(screen,(255,0,0),(rx,ry),10)


    def draw(self, steer = 0):


        if steer == 0:

            if self.degree == -359 or self.degree == 359:
                self.degree = 0
            
            angle = -1*self.degree + 90


            radian = math.radians(angle)



            add_x = self.speed * math.cos(radian)
            add_y = self.speed * math.sin(radian)
            
            
            self.barx1 += add_x
            self.bary1 -= add_y

            self.barx2 += add_x
            self.bary2 -= add_y


            self.left_wheel_x = self.barx1
            self.left_wheel_y = self.bary1

            self.right_wheel_x = self.barx2
            self.right_wheel_y = self.bary2



            self.draw_rod(self.barx1,self.bary1,self.barx2,self.bary2)
            self.draw_tire(self.left_wheel_x,self.left_wheel_y,self.right_wheel_x,self.right_wheel_y)

        elif steer == 1:

            if self.degree == -359 or self.degree == 359:
                self.degree = 0
            else:
                self.degree += 1

            angle = math.radians(self.degree + 180)

            change_x = self.length * math.cos(angle)
            change_y = self.length * math.sin(angle)

            self.barx1 = self.barx2+change_x
            self.bary1 = self.bary2+change_y

            


            self.left_wheel_x = self.barx1
            self.left_wheel_y = self.bary1

            self.draw_rod(self.barx1,self.bary1,self.barx2,self.bary2)
            self.draw_tire(self.left_wheel_x,self.left_wheel_y,self.right_wheel_x,self.right_wheel_y)


        elif steer == -1:

            angle = math.radians(self.degree)
            change_x = self.length * math.cos(angle)
            change_y = self.length * math.sin(angle)

            self.barx2 = self.barx1+change_x
            self.bary2 = self.bary1+change_y

            if self.degree == -359 or self.degree == 359:
                self.degree = 0
            else:
                self.degree -= 1


            self.right_wheel_x = self.barx2
            self.right_wheel_y = self.bary2


            self.draw_rod(self.barx1,self.bary1,self.barx2,self.bary2)
            self.draw_tire(self.left_wheel_x,self.left_wheel_y,self.right_wheel_x,self.right_wheel_y)



rotate = 0
    

while running:

    screen.fill("purple")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            rods.append(Rod())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rotate = -1
            elif event.key == pygame.K_RIGHT:
                rotate = 1
            elif event.key == pygame.K_UP:
                rotate = 0
        
    

    for i in rods:
        i.draw(rotate)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()