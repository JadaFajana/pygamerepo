import pygame
pygame.init()

background = pygame.display.set_mode((650, 500))

background.fill((100,250,100))


#for red.png
image_red = pygame.image.load('red.png.png')
x = 0
y = 0

#for green.png
image_green = pygame.image.load('green.png.png')
x_green = 0
y_green = 500 - 80

clock = pygame.time.Clock()

#player movement
x_direction = "right"
player_y = 0
playerRight = False
playerLeft = False
playerUp = False
playerDown = False

run = True
while run:
    for i in pygame.event.get():player_x = 0
    for event in pygame.event.get():   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerLeft = True
            if event.key == pygame.K_RIGHT:
                playerRight = True
            if event.key == pygame.K_UP:
                playerUp = True  
            if event.key == pygame.K_DOWN:
                playerDown = True  
        if event.type == pygame.KEYUP:
            playerLeft = False
            playerRight = False
            playerUp = False
            playerDown = False

    #making movement of player
    if playerRight:
        player

        if i.type == pygame.QUIT:
            exit()
    background.blit(image_red, (x,y))
    
    if x >= 650 - image_red.get_width():
        x_direction = "left"
    if x == 10:
        x_direction = "right"
    if x_direction == "right":
        x += 1
    else:
        x -= 1
    clock.tick(150)
    pygame.display.update()
    
    background.fill((100,250,100))

    background.blit(image_green, (x_green,y_green))



            
