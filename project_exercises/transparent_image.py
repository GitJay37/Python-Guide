<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Transparent image")


#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black
my_color = (62, 187, 187)

image = pygame.image.load("images/trunks.jpg")
rect1 = image.get_rect()
rect1.center = (width // 2, heigth // 2)

surface1= pygame.Surface( (rect1.width, rect1.height), pygame.SRCALPHA )
surface1.fill( (0, 0, 0, 50) )
rect1 = surface1.get_rect()
rect1.center = rect1.center


font = pygame.font.Font("fonts/KaushanScript-Regular.ttf", 32)

while True: 
    for event in pygame.event.get(): #Recorrer todos los eventos
        if event.type == pygame.QUIT: #Close window
            pygame.quit() #Finish library
            sys.exit() #Finish library

        surface.fill(my_color)

        surface.blit(image, rect1)
        surface.blit(surface1, rect1)

        pygame.display.update()
=======
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Transparent image")


#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black
my_color = (62, 187, 187)

image = pygame.image.load("images/trunks.jpg")
rect1 = image.get_rect()
rect1.center = (width // 2, heigth // 2)

surface1= pygame.Surface( (rect1.width, rect1.height), pygame.SRCALPHA )
surface1.fill( (0, 0, 0, 50) )
rect1 = surface1.get_rect()
rect1.center = rect1.center


font = pygame.font.Font("fonts/KaushanScript-Regular.ttf", 32)

while True: 
    for event in pygame.event.get(): #Recorrer todos los eventos
        if event.type == pygame.QUIT: #Close window
            pygame.quit() #Finish library
            sys.exit() #Finish library

        surface.fill(my_color)

        surface.blit(image, rect1)
        surface.blit(surface1, rect1)

        pygame.display.update()
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
    