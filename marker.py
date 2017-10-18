import pygame as pg
import setting
class Marker(pg.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.image = pg.Surface((200,500))
        self.rect = self.image.get_rect()
        self.rect.topright = (800,0)
a = Marker()
pg.init()
screen = pg.display.set_mode((800,500))
while 1:
    screen.fill((0,0,0))

