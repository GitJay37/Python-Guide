<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Collision")


#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black
my_color = (62, 187, 187)

rect1 = pygame.Rect(0, 0, 100, 80)
rect1.center = (width // 2, heigth // 2)

rect2 = pygame.Rect(0, 0, 100, 80)

font = pygame.font.Font("fonts/KaushanScript-Regular.ttf", 32)

while True: 
    for event in pygame.event.get(): #Recorrer todos los eventos
        if event.type == pygame.QUIT: #Close window
            pygame.quit() #Finish library
            sys.exit() #Finish library

        surface.fill(my_color)

        rect2.center = pygame.mouse.get_pos()

        pygame.draw.rect(surface, white, rect1)
        pygame.draw.rect(surface, black, rect2)

        message = ""    

        if rect1.colliderect(rect2):
            message = "There is a collision!!"

        text = font.render(message, True, red)

        rect3 = text.get_rect()
        rect3.midtop = (width // 2, 50)

        surface.blit(text, rect3)
        pygame.display.update()
=======
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Collision")


#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black
my_color = (62, 187, 187)

rect1 = pygame.Rect(0, 0, 100, 80)
rect1.center = (width // 2, heigth // 2)

rect2 = pygame.Rect(0, 0, 100, 80)

font = pygame.font.Font("fonts/KaushanScript-Regular.ttf", 32)

while True: 
    for event in pygame.event.get(): #Recorrer todos los eventos
        if event.type == pygame.QUIT: #Close window
            pygame.quit() #Finish library
            sys.exit() #Finish library

        surface.fill(my_color)

        rect2.center = pygame.mouse.get_pos()

        pygame.draw.rect(surface, white, rect1)
        pygame.draw.rect(surface, black, rect2)

        message = ""    

        if rect1.colliderect(rect2):
            message = "There is a collision!!"

        text = font.render(message, True, red)

        rect3 = text.get_rect()
        rect3.midtop = (width // 2, 50)

        surface.blit(text, rect3)
        pygame.display.update()
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
    