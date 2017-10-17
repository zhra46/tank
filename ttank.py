import pygame
class Tank1(pygame.sprite.Sprite):
    def __init__(self,x=50,y=50):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.imgs = []
        self.speed = 10
        self.direction = ['U','R','D','L']
        self.direct = 0
        self.image = pygame.image.load('tank-images/tankU.gif')
        for direct in self.direction:
            img = pygame.image.load('tank-images/tank%s.gif'%direct)
            self.imgs.append(img)
        self.image = self.imgs[self.direct]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        print (self.image)
    def setDirection(self,direction):
        self.direct = direction
    def move(self,direct):
        if direct == '0':
            self.y -=self.speed
        if direct == '1':
            self.x += self.speed
        if direct =='2':
            self.y += self.speed
        if direct =='3':
            self.x -= self.speed

    def update(self):
        self.image = self.imgs[self.direct]
        # self.direct+=1
        # if self.direct >=len(self.direction):
        #     self.direct = 0
