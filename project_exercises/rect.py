<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Rect")

rect = pygame.Rect(100, 150, 120, 60)
rect.center = (width // 2, heigth // 2)
rect1 = (100, 100, 80, 40) #Para interactuar mejor es importar la clase Rect
print("Rect's left value: ", rect.left, "and", "Rect's top value: ", rect.top)
#print("Rect1's left value: ", rect1.left, "and", "Rect1's top value: ", rect1.top)

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
    
    pygame.draw.rect(surface, my_color, rect)
    pygame.draw.rect(surface, red, rect1)

=======
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Rect")

rect = pygame.Rect(100, 150, 120, 60)
rect.center = (width // 2, heigth // 2)
rect1 = (100, 100, 80, 40) #Para interactuar mejor es importar la clase Rect
print("Rect's left value: ", rect.left, "and", "Rect's top value: ", rect.top)
#print("Rect1's left value: ", rect1.left, "and", "Rect1's top value: ", rect1.top)

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
    
    pygame.draw.rect(surface, my_color, rect)
    pygame.draw.rect(surface, red, rect1)

>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
    pygame.display.update()