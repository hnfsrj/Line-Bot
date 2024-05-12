
import math


def init(py, scr, cir, Circ):
    global pygame,screen,circles, Circle

    pygame = py
    screen = scr
    circles = cir
    Circle = Circ





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




class Sensor(Tires):
    
    def __init__(self):
        super().__init__()

        self.sensor_x = self.x
        self.sensor_y = self.y
        self.sensor_size = 5
        self.time = 20
        self.timer = 0
        self.first = True
        self.set = False
        self.history = 0

    def draw_sensor(self):
        pygame.draw.circle(screen,(0,0,255),(self.sensor_x,self.sensor_y),self.sensor_size)



    def sensing(self):

        collision_distance = self.sensor_size + Circle.radius

        for i in circles:
            distance_in_between =  math.sqrt(math.pow((i.position[0] - self.sensor_x),2)+math.pow((i.position[1] - self.sensor_y),2))
            
            if distance_in_between <= collision_distance:
                self.timer = 0
                return 0
            

        if not self.first:
            return self.rotation
        
        if self.timer < self.time:
            self.timer += 1
            return -1
        else:
            return 1


          

class Robot(Sensor):
    
    def draw(self):

        steer = self.sensing()
        self.steering(steer)

        self.draw_rod()
        self.draw_tire()
        self.draw_sensor()

    def steering(self, steer):

        if self.degree == -359 or self.degree == 359:
            self.degree = 0



        if steer == 1:

            self.last_steer = 1

            self.degree += 1

            angle = math.radians(self.degree + 180)

            change_x = self.length * math.cos(angle)
            change_y = self.length * math.sin(angle)

            self.barx1 = self.barx2+change_x
            self.bary1 = self.bary2+change_y

            if self.first:
                self.history = 1
                self.set = True


        elif steer == -1:

            self.last_steer = -1

            self.degree -= 1

            angle = math.radians(self.degree)
            
            change_x = self.length * math.cos(angle)
            change_y = self.length * math.sin(angle)

            self.barx2 = self.barx1+change_x
            self.bary2 = self.bary1+change_y

            if self.first:
                self.history = -1
                self.set = True

        else:

            angle = math.radians(-1*self.degree + 90)

            add_x = self.speed * math.cos(angle)
            add_y = self.speed * math.sin(angle)

            self.barx1 += add_x
            self.bary1 -= add_y

            self.barx2 += add_x
            self.bary2 -= add_y

            if self.set:
                self.rotation = self.history
                self.set = False
                self.first = False
                
        

        s_angle = math.radians(-1*self.degree + 90)

        s_add_x = 30 * math.cos(s_angle)
        s_add_y = 30 * math.sin(s_angle)

        self.sensor_x = (self.barx1 + self.barx2)/2 + s_add_x
        self.sensor_y = (self.bary1 + self.bary2)/2 - s_add_y

