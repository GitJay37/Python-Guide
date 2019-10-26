<<<<<<< HEAD
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Background sound")

#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black
my_color = (62, 187, 187)

# 1. Obtener una fuente
pygame.mixer.music.load("sounds/Hooked on a Feeling.mp3") # -> Make a surface
pygame.mixer.music.set_volume(0.5) #Volume from min 0.0 to 1.0 value float
pygame.mixer.music.play(2, 0.0)
pygame.mixer.music.fadeout(60000)
while True: 
    for event in pygame.event.get(): #Recorrer todos los eventos
        if event.type == pygame.QUIT: #Close window
            pygame.quit() #Finish library
            sys.exit() #Finish library
    
    surface.fill(black)
    pygame.display.update()
=======
import sys
import pygame
pygame.init()

width = 400
heigth = 500

surface = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Background sound")

#RGB
red = pygame.Color(255, 0, 0) #Red
green = pygame.Color(0, 255, 0) #Green
blue = pygame.Color(0, 0, 255) #Blue
white = pygame.Color(255, 255, 255) #White
black = pygame.Color(0, 0, 0) #Black
my_color = (62, 187, 187)

# 1. Obtener una fuente
pygame.mixer.music.load("sounds/Hooked on a Feeling.mp3") # -> Make a surface
pygame.mixer.music.set_volume(0.5) #Volume from min 0.0 to 1.0 value float
pygame.mixer.music.play(2, 0.0)
pygame.mixer.music.fadeout(60000)
while True: 
    for event in pygame.event.get(): #Recorrer todos los eventos
        if event.type == pygame.QUIT: #Close window
            pygame.quit() #Finish library
            sys.exit() #Finish library
    
    surface.fill(black)
    pygame.display.update()
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
    