import time
import pygame 
import math

pygame.init()
WIDTH=1000
HEIGHT=500

wave = [[350, 250]]

timestamp = time.time()
t = 0
y = 0

cNum = 20

screen = pygame.display.set_mode([WIDTH, HEIGHT])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    newTime = time.time()
    t = newTime - timestamp
    print(t)


    screen.fill((0, 0, 0))
    #------------------
    x = 250 + 100*math.cos(t)
    y = 250 + 100*math.sin(t)

    xWave = 350 + 20 * t

    if (len(wave) > 500):
        wave.pop()


    #print(wave)
    pygame.draw.circle(screen, (255, 255, 255), (250, 250), 100, width = 1)
    #pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)


    for i in range(1, cNum, 2):
        prevx = x
        prevy = y

        n = i * 2 + 1
        radius = 100 * (4/(n*math.pi))
        x += radius * math.cos(n * t)
        y += radius * math.sin(n * t)
        
        pygame.draw.circle(screen, (255, 255, 255), (prevx, prevy), radius, width = 1)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)

        if i == cNum -1:
            wave.insert(0 ,[xWave, y])
            pygame.draw.aalines(screen, (255, 255, 255), False, wave)

        
    

    #pygame.draw.aaline(screen, (255, 255, 255), (250, 250), (x,y))
    pygame.draw.aaline(screen, (255, 0, 255), (x, y), (wave[0]))


    #----------------
    time.sleep(0.05)
    pygame.display.flip()
pygame.quit()