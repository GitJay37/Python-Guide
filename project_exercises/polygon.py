<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Polygon")

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
    #Triangulo
    pygame.draw.polygon(surface, red, ( (0, 400), (100, 300), (200, 400) ) )
    #Pentagono
    pygame.draw.polygon(surface, my_color,
        ( 
            (146, 0), 
            (291, 106), 
            (236, 277), 
            (56, 277), 
            (0, 106)
        ) 
    )
    pygame.display.update()
=======
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Polygon")

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
    #Triangulo
    pygame.draw.polygon(surface, red, ( (0, 400), (100, 300), (200, 400) ) )
    #Pentagono
    pygame.draw.polygon(surface, my_color,
        ( 
            (146, 0), 
            (291, 106), 
            (236, 277), 
            (56, 277), 
            (0, 106)
        ) 
    )
    pygame.display.update()
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
    