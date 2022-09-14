import pygame
# initialization
pygame.init()

# Screen Size
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('space.png')
playerX = 370
playerY = 480
playerX_change = 0




def player(x,y):
        screen.blit(playerImg, (x, y))


running = True 
while running:
        
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            print("keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerY_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerY_change = 0
        
        playerX += playerX_change
        player(playerX,playerY)
        pygame.display.update()
            
