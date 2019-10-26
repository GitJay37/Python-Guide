<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Move image")

image = pygame.image.load("images/small_pic}.jpg")
rect = image.get_rect()
rect.center = (width // 2, heigth // 2)

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
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        rect.y -= 5
    if pressed[pygame.K_a]:
        rect.x -= 5
    if pressed[pygame.K_d]:
        rect.x += 5
    if pressed[pygame.K_s]:
        rect.y += 5
    
    #Validations
    
    if rect.left < 0:
        rect.left = 0

    if rect.right > width:
        rect.right = width

    if rect.top < 0:
        rect.top = 0

    if rect.bottom > heigth:
        rect.bottom = heigth

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

image = pygame.image.load("images/small_pic}.jpg")
rect = image.get_rect()
rect.center = (width // 2, heigth // 2)

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
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        rect.y -= 5
    if pressed[pygame.K_a]:
        rect.x -= 5
    if pressed[pygame.K_d]:
        rect.x += 5
    if pressed[pygame.K_s]:
        rect.y += 5
    
    #Validations
    
    if rect.left < 0:
        rect.left = 0

    if rect.right > width:
        rect.right = width

    if rect.top < 0:
        rect.top = 0

    if rect.bottom > heigth:
        rect.bottom = heigth

    surface.fill(black)
    surface.blit(image, rect)
    pygame.display.update()
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
    