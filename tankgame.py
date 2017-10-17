import pygame as pg
import eventdetector,ttank
import setting as s
class Tankgame(object):
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(s.res)
        pg.display.set_caption('Tank Game')
        self.ed = eventdetector.Eventdetect()
        self.player = ttank.Tank1()
    def handleEvent(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.direct = 0
                if event.key == pg.K_RIGHT:
                    self.player.direct = 1
                if event.key == pg.K_DOWN:
                    self.player.direct = 2
                elif event.key == pg.K_LEFT:
                    self.player.direct = 3
    def run(self):
        while True:
            #self.update((self.player.image,self.player.rect))
            self.screen.fill(s.backgroundcolor)
            self.screen.blit(self.player.image,self.player.rect)
            self.player.update()
            self.handleEvent()
            pg.display.update()
    def update(self,*args):
        self.screen.fill(s.backgroundcolor)
        for i in args:
            self.screen.blit(i[0],i[1])
        pg.display.update()

game = Tankgame()
game.run()
