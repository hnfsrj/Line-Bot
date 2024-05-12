
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
        self.step = math.radians(1)

    def draw_rod(self,bx1,by1,bx2,by2):
        pygame.draw.line(screen, (255,255,255), (bx1,by1), (bx2,by2),5)

    def draw_tire(self,lx,ly,rx,ry):
        pygame.draw.circle(screen,(255,0,0),(lx,ly),10)
        pygame.draw.circle(screen,(255,0,0),(rx,ry),10)


    def draw(self, steer = 0):

        #length of the rod
        # print(math.sqrt(pow((self.bary2 - self.bary1),2)+pow((self.barx2 - self.barx1),2)))

        if steer == 0:

            angle = math.degrees(math.atan((self.bary2 - self.bary1) / (self.barx2 - self.barx1))) - 90

            measurey = self.bary2 - self.bary1
            measurex = self.barx2 - self.barx1

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

            radian = math.radians(angle)
            # degree = math.degrees(radian)





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
            if self.direction == 1:
                self.bary1 -= self.speed

                measurey = self.bary1 - self.bary2

                if measurey <= (-1*self.radius):
                    self.bary1 += (1 * self.speed)
                    self.direction *= -1

            else:
                self.bary1 += self.speed

                measurey = self.bary1 - self.bary2

                if measurey >= self.radius:
                    self.bary1 -= (1 * self.speed)
                    self.direction *= -1



            
            if self.direction == 1:
                next_x = -1*math.sqrt(math.pow(self.radius,2) - math.pow((self.bary1 - self.bary2),2)) + self.barx2
            else:
                next_x = math.sqrt(math.pow(self.radius,2) - math.pow((self.bary1 - self.bary2),2)) + self.barx2

            
            dist = math.sqrt(pow((self.bary2 - self.bary1),2)+pow((self.barx2 - next_x),2))

            if dist<self.length:
                difference = self.length - dist

                #add of subtract from next_x(barx1) and bary1

                if self.direction == 1:
                    next_x -= difference
                else:
                    next_x += difference
            
            self.barx1 = next_x
            
            self.left_wheel_x = self.barx1
            self.left_wheel_y = self.bary1


            self.draw_rod(self.barx1,self.bary1,self.barx2,self.bary2)
            self.draw_tire(self.left_wheel_x,self.left_wheel_y,self.right_wheel_x,self.right_wheel_y)


        elif steer == -1:

            cx = self.barx1
            cy = self.bary1

            px = self.barx2
            py = self.bary2


            el = 2*math.pow(self.length,2)*(1-math.cos(self.step))

            r = math.pow(el,2) - math.pow(px,2) - math.pow(py,2)
            t = math.pow(self.length,2) - math.pow(cx,2) - math.pow(cy,2)

            q = (r-t)/(2*(cx-px))
            n = (cy - py)/(cx - px)

            k = math.pow(n,2) + 1
            l = (2*q*n) + (2*px*n) - (2*py)
            m = r - math.pow(q,2) + (2*px*q)

            y = ((-1*l)-(math.sqrt((math.pow(l,2))+(4*k*m))))/(2*k)
            # y = ((-1*l)-(math.sqrt((math.pow(l,2))+(4*k*m))))/(2*k)

            x = q - (n*y)



            self.barx2 = x
            self.bary2 = y




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
        if rotate == 1:
            i.draw(rotate)
        else:
            i.draw(rotate)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()