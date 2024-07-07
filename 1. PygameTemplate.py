"""
Pygame Template


   Import
   Initialize
   Create Window
   Initialize clock for FPS

   Loop
       Get events
           if quit
                quit pygame
       Apply Logic
       Update Display/Window
       Set FPS

"""

# Import
import pygame

#Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")

#Initialize Clock For FPS
fps = 30
clock = pygame.time.Clock()

#Main Loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    #   Apply logic
    window.fill((255, 255, 255))

    #Update Display
    pygame.display.update()
    #set FPS
    clock.tick(fps)