import sys
import pygame

pygame.init()
window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Block")

rect = pygame.Rect(0, 0, 20, 20)
en = pygame.Rect(200,10, 100,50)
rect.center = window.get_rect().center
vel = 5

def initate():
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.draw.rect(window, (0, 255, 0), en)

def movement():
    keys = pygame.key.get_pressed()
    
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
        
    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit
                sys.exit()
                



    window.fill(0)

    #Do stuff here that you wnant to be infront of the game:
    movement() #movement
    initate() #should be used for the initiation of stuff
    pygame.display.flip()

