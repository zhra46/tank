import pygame as pg
import setting
class Bullet(pg.sprite.Sprite):
    def __init__(self,tank):
        pg.sprite.Sprite.__init__(self)
        self.speed = 20
        self.imgs = []
        for i in ['U','R','D','L']:
            self.imgs.append(pg.image.load('./tank-images/missile%s.gif'%i))
        self.direct = tank.direct
        self.image = self.imgs[self.direct]
        self.rect = self.image.get_rect()
        if self.direct == 0:
            self.rect.center = tank.rect.midtop
        if self.direct == 1:
            self.rect.center = tank.rect.midright
        if self.direct == 2:
            self.rect.center = tank.rect.midbottom
        if self.direct == 3:
            self.rect.center = tank.rect.midleft
    def update(self):
        if self.direct ==0:
            self.rect.centery -=self.speed
        if self.direct ==1:
            self.rect.centerx +=self.speed
        if self.direct ==2:
            self.rect.centery +=self.speed
        if self.direct ==3:
            self.rect.centerx -=self.speed
class BulletGroup(pg.sprite.Group):
    def __init__(self,*args):
        pg.sprite.Group.__init__(self)
    def check(self):
        for bullet in self.copy():
            if bullet.rect.bottom<0 or bullet.rect.top>setting.height or bullet.rect.left<0 or bullet.rect.right>setting.width:
                self.remove(bullet)
            print (len(self))