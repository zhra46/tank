import pygame
class Boom(pygame.sprite.Sprite):
    def __init__(self,sprite):
        super().__init__()
        imgs=[]
        for i in range(11):
            img =pygame.image.load('tank-images/%s.gif'%i)
            img_rect = img.get_rect()
            img_rect.center = (200,200)
            imgs.append(img)
        self.imgs = imgs
        self.image = self.imgs[0]
        self.rect = self.image.get_rect()
        self.count = 0
        self.sprite = sprite
    def update(self):
        if self.count >=10:
            self.kill()
        self.image = self.imgs[self.count]
        self.rect = self.image.get_rect()
        self.rect.center = self.sprite.rect.center
        self.count +=1
    # def testshow(self):
    #     while 1:
    #         e.keydetect(tank=0)
    #         clk.tick(15)
    #         rect = self.imgs[i].get_rect()
    #         x,y = 0,0
    #         rect.center = self.des.center
    #         screen.blit(self.imgs[i],rect)
    #         pygame.display.update()
    #         screen.fill((255,255,255))
    #         i +=1
    #         if i >=len(self.imgs):
    #             break
    #         x += 2
    #         y += 1
