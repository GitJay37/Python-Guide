<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Rect")

#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black
my_color = (62, 187, 187)

while True: 
    for event in pygame.event.get(): #Recorrer todos los eventos
        if event.type == pygame.QUIT: #Close window
            pygame.quit() #Finish library
            sys.exit() #Finish library
    
    surface.fill(black)
    
    #1 Donde se pintará la figura
    #2Color de la figura
    #3 tupla x and y radio 
    pygame.draw.rect(surface, red, (60, 80, 50, 70))
    pygame.draw.circle(surface, blue, (200, 200), 100) 
    pygame.draw.line(surface, green, (100, 100), (200, 350), 3 )
=======
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Rect")

#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black
my_color = (62, 187, 187)

while True: 
    for event in pygame.event.get(): #Recorrer todos los eventos
        if event.type == pygame.QUIT: #Close window
            pygame.quit() #Finish library
            sys.exit() #Finish library
    
    surface.fill(black)
    
    #1 Donde se pintará la figura
    #2Color de la figura
    #3 tupla x and y radio 
    pygame.draw.rect(surface, red, (60, 80, 50, 70))
    pygame.draw.circle(surface, blue, (200, 200), 100) 
    pygame.draw.line(surface, green, (100, 100), (200, 350), 3 )
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
    pygame.display.update()