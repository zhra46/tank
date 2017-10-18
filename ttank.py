import pygame
import setting as s
from bullet import *
import random
import boom
class Tank1(pygame.sprite.Sprite):
    def __init__(self,x=50,y=50):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.flag = [0,0,0,0]
        self.imgs = []
        self.speed = s.tank_move_speed
        self.direction = ['U','R','D','L']
        self.direct = 0
        self.image = pygame.image.load('tank-images/tankU.gif')
        for direct in self.direction:
            img = pygame.image.load('tank-images/tank%s.gif'%direct)
            self.imgs.append(img)
        self.image = self.imgs[self.direct]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
    def setDirection(self,direction):
        self.direct = direction
    def move(self,direct):
        if direct == 0:
            self.flag = [1,0,0,0]
        elif direct == 1:
            self.flag = [0,1,0,0]
        elif direct == 2:
            self.flag = [0,0,1,0]
        elif direct == 3:
            self.flag = [0,0,0,1]
    def stop(self,direct):
        if direct == 0:
            self.flag[0] = 0
        if direct == 1:
            self.flag[1] = 0
        if direct == 2:
            self.flag[2] = 0
        if direct == 3:
            self.flag[3] = 0
    def fire(self):
        return Bullet(self)
    def isoutbound(self):
        if self.rect.top<0:
            self.rect.top = 0
            return True
        if self.rect.left <0:
            self.rect.left = 0
            return True
        if self.rect.bottom > s.height:
            self.rect.bottom = s.height
            return True
        if self.rect.right >s.width:
            self.rect.right = s.width
            return True
        else:
            return False
    def boom(self):
        self.kill()
        return (boom.Boom(self))
    def update(self):
        self.image = self.imgs[self.direct]
        if self.flag[0] == 1:
            self.direct = 0
            if self.rect.top < 0:
                self.rect.top =300
            else:
                self.rect.centery -= self.speed
        if self.flag[1] == 1:
            self.direct = 1
            if self.rect.right >= s.width:
                pass
            else:
                self.rect.centerx += self.speed
        if self.flag[2] == 1:
            self.direct = 2
            if self.rect.bottom >= s.height:
                pass
            else:
                self.rect.centery += self.speed
        if self.flag[3] == 1:
            self.direct = 3
            if self.rect.left <=0:
                pass
            else:
                self.rect.centerx -= self.speed

        # self.direct+=1
        # if self.direct >=len(self.direction):
        #     self.direct = 0\
class Tank2(Tank1):
    def __init__(self,*args):
        super().__init__(*args)
        self.foward = random.randint(1,10)
        self.direct = random.randint(1,3)

    def update(self):
        if self.foward <=0:
            self.foward = random.randint(5,15)
            self.direct = random .randint(0,3)
        else:
            self.foward -=1
            if self.isoutbound():
                self.foward = 0
            if self.direct == 0:
                self.image = self.imgs[self.direct]
                self.rect.centery -= s.tank_move_speed
            if self.direct == 1:
                self.image = self.imgs[self.direct]
                self.rect.centerx += s.tank_move_speed

            if self.direct == 2:
                self.image = self.imgs[self.direct]
                self.rect.centery += s.tank_move_speed
            if self.direct == 3:
                self.image = self.imgs[self.direct]
                self.rect.centerx -= s.tank_move_speed
class Tankfac(object):
    @staticmethod
    def buildtank():
        x = random.randint(0,s.width)
        y = random.randint(0,s.height/2)
        return Tank2(x,y)
