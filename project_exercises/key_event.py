<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Key Event")

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
        if event.type == pygame.QUIT: #Close window
            pygame.quit() #Finish library
            sys.exit() #Finish library
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                message = "Left"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                message = "Right"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                message = "Down"
            if event.key == pygame.K_UP or event.key == pygame.K_w: 
                message = "Up!!!"
            print(message)
        if event.type == pygame.KEYUP:
            print("button without function")

    pygame.display.update()
    
=======
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Key Event")

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
        if event.type == pygame.QUIT: #Close window
            pygame.quit() #Finish library
            sys.exit() #Finish library
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                message = "Left"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                message = "Right"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                message = "Down"
            if event.key == pygame.K_UP or event.key == pygame.K_w: 
                message = "Up!!!"
            print(message)
        if event.type == pygame.KEYUP:
            print("button without function")

    pygame.display.update()
    
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
