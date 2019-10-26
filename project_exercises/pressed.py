<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Method Get Pressed")

#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black
my_color = (62, 187, 187)

# 1. Obtener una fuente
while True: 
    for event in pygame.event.get(): #Recorrer todos los eventos
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w]:
            print("UP")
        if pressed[pygame.K_a]:
            print("LEFT")
        if pressed[pygame.K_d]:
            print("RIGHT")
        if pressed[pygame.K_s]:
            print("DOWN")

    surface.fill(my_color)
=======
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Method Get Pressed")

#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black
my_color = (62, 187, 187)

# 1. Obtener una fuente
while True: 
    for event in pygame.event.get(): #Recorrer todos los eventos
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w]:
            print("UP")
        if pressed[pygame.K_a]:
            print("LEFT")
        if pressed[pygame.K_d]:
            print("RIGHT")
        if pressed[pygame.K_s]:
            print("DOWN")

    surface.fill(my_color)
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
    pygame.display.update()