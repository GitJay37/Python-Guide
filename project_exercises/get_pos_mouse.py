<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Mouse event")

font = pygame.font.Font("fonts/KaushanScript-Regular.ttf", 32)

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
    
    pos_x, pos_y = pygame.mouse.get_pos() # tupla x, y
    message = "pos x : {} pos y: {}".format(pos_x, pos_y)

    text = font.render(message, True, my_color)
    rect = text.get_rect()
    rect.center = (width // 2, heigth // 2)

    surface.fill(black)
    surface.blit(text, rect)
    pygame.display.update()
=======
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Mouse event")

font = pygame.font.Font("fonts/KaushanScript-Regular.ttf", 32)

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
    
    pos_x, pos_y = pygame.mouse.get_pos() # tupla x, y
    message = "pos x : {} pos y: {}".format(pos_x, pos_y)

    text = font.render(message, True, my_color)
    rect = text.get_rect()
    rect.center = (width // 2, heigth // 2)

    surface.fill(black)
    surface.blit(text, rect)
    pygame.display.update()
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
    