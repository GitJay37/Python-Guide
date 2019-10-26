<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Move image")

image = pygame.image.load("images/dbz.jpg")
rect = image.get_rect()
rect.center = (width // 2, heigth // 2)

#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black

    surface.fill(black)
    surface.blit(image, rect)
    pygame.display.update()
=======
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Move image")

image = pygame.image.load("images/dbz.jpg")
rect = image.get_rect()
rect.center = (width // 2, heigth // 2)

#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black

    surface.fill(black)
    surface.blit(image, rect)
    pygame.display.update()
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
    