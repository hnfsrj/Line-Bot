
import path
import robot

import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


bots = []
circles = []

path.init(pygame,screen)
robot.init(pygame,screen,circles,path.Circle)


record = False

mode = 1



while running:

    screen.fill("purple")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode == 1:
                record = True
            else:
                bots.append(robot.Robot())

        elif event.type == pygame.MOUSEBUTTONUP:
            if mode == 1:
                record = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LCTRL:
                mode *= -1
        
    
    if record:
        circles.append(path.Circle())


    for i in circles:
        i.draw()

    for i in bots:
        i.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()