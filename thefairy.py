import pygame

#initiate pygame
pygame.init()

#create a window
background = pygame.display.set_mode((650, 500))

#color/forest of background
forest = pygame.transform.scale(pygame.image.load('forest.png'), (650, 500))

#Image for fairy
image = pygame.image.load('fairy.png')
x = 0 
y = 0



clock = pygame.time.Clock()


run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    background.blit(forest, (0,0))
    

    background.blit(image, (x,y)) #make the image move
    pygame.display.flip()
    x += 1
    y += 1
    clock.tick(80)

    if x == 650:
        x = 0
        y = 0

    
