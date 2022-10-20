import pygame,sys


pygame.init()
Clock = pygame.time.Clock()
FPS = 60
size = [1000,800]
bg = [0,0,0]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Movement')


class Buscemi(): 

    
    def draw(self):                                             
        return pygame.draw.rect(screen,"blue",(100,80,1000,50))    

  

class bullet():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self,x,y):
        pygame.draw.rect(screen,"white",(y,x,1,3))



class Player:
    def __init__(self,vel,x,y,buscemi): 
        self.vel = vel
        self.buscemi=buscemi

        self.x = x
        self.y = y
        self.xold = None    
        self.yold = None    
        self.jump = False
        self.draw()     

    def move(self):
        k = pygame.key.get_pressed()


        if not self.dude.colliderect(self.buscemi.draw()):
            self.xold = self.x  
            self.yold = self.y  
            if k[pygame.K_a] or k[pygame.K_LEFT]:
                self.x -= self.vel
            if k[pygame.K_d] or k[pygame.K_RIGHT]:
                self.x += self.vel
            if k[pygame.K_w] or k[pygame.K_UP]:
                self.y -= self.vel
            if k[pygame.K_s] or k[pygame.K_DOWN]:
                self.y += self.vel
        else:   
            self.x = self.xold  
            self.y = self.yold  
  

    def draw(self):
        self.dude = pygame.draw.rect(screen,"red",(self.x,self.y,50,50))    

    def bordercollsion(self):
        if self.x <=0:
            self.x=0
        if self.x >=950:
            self.x=950
        if self.y <=0:
            self.y=0
        if self.y >=750:
            self.y=750
        
        

    def do(self):
        self.move()
        self.draw()
        self.bordercollsion()
        
    

en = Buscemi()  
player = Player(.5,500,600,en)   

while True:
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit
                sys.exit()
        

    player.do()
    pygame.display.update()