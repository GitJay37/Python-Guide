<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Mouse event")

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

        if event.type == pygame.MOUSEBUTTONUP:
            print("Click ok!", event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Without click")

    surface.fill(my_color)
    pygame.display.update()

# print(event.pos) position clic mouse
=======
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Mouse event")

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

        if event.type == pygame.MOUSEBUTTONUP:
            print("Click ok!", event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Without click")

    surface.fill(my_color)
    pygame.display.update()

# print(event.pos) position clic mouse
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
# event mouse Clic == 1, left, 2=center, 3= rigth, 4 scroll up, 5 scrol down