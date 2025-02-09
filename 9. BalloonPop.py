# Import
import random
import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time


#Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Pop")

#Initialize Clock For FPS
fps = 30
clock = pygame.time.Clock()

#webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280) # width
cap.set(4, 720) # height

# Images
#imgBackground = pygame.image.load('../Resorces/BackgroundBlue.jpg').convert()
imgBalloon = pygame.image.load('../Resources/BalloonRed.png').convert_alpha()
rectBalloon = imgBalloon.get_rect()
rectBalloon.x, rectBalloon.y = 500, 300

# Variables
speed = 50
score = 0
startTime = time.time()
totalTime = 60



# detector
detector = HandDetector(detectionCon =0.8, maxHands=1)

def resetBalloon():
    rectBalloon.x = random.randint(100, img.shape[1]-100)
    rectBalloon.y = img.shape[0]+50

#Main Loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    #   Apply logic
    timeRemain = int(totalTime -(time.time() - startTime))
    if timeRemain < 0:
        window.fill((255, 255, 255))

        font = pygame.font.Font(None, 50)
        textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time UP', True, (50, 50, 255))
        window.blit(textScore, (450, 350))
        window.blit(textTime, (530, 275))
    else:

        # OpenCV
        success, img = cap.read()
        hands, img = detector.findHands(img)

        rectBalloon.y -= speed

        if rectBalloon.y < 0:
           resetBalloon()
           speed += 1

        if hands:
           hand = hands[0]
           x, y = hand['lmList'][8][0:2]
           if rectBalloon.collidepoint(x, y):
              resetBalloon()
              score +=10
              speed +=1

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        # frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))


        window.blit(imgBalloon, rectBalloon)

        font = pygame.font.Font(None, 50)
        textScore = font.render(f'Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
        window.blit(textScore, (35, 35))
        window.blit(textTime, (1000, 35))


    #Update Display
    pygame.display.update()
    #set FPS
    clock.tick(fps)