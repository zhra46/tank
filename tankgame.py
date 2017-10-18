import pygame as pg
import ttank,bullet
import setting as s
class Tankgame(object):
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(s.res)
        self.screen_rect = self.screen.get_rect()
        self.live = 3
        pg.display.set_caption('Tank Game')
        self.player = ttank.Tank1(self.screen_rect.centerx,self.screen_rect.bottom-20)
        self.playerg = pg.sprite.Group()
        self.playerg.add(self.player)
        self.clock = pg.time.Clock()
        self.bltgrp = pg.sprite.Group()
        self.enemy = pg.sprite.Group()
        self.booms = pg.sprite.Group()
        self.ebltgrp = bullet.BulletGroup()
    def handleEvent(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.USEREVENT+1:
                for i in self.enemy:
                    self.ebltgrp.add(i.fire())
            if event.type == pg.USEREVENT+2:
                self.enemy.add(ttank.Tankfac.buildtank())
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.move(0)
                if event.key == pg.K_RIGHT:
                    self.player.move(1)
                if event.key == pg.K_DOWN:
                    self.player.move(2)
                elif event.key == pg.K_LEFT:
                    self.player.move(3)
                elif event.key ==pg.K_SPACE:
                    self.bltgrp.add(self.player.fire())
                elif event.key == pg.K_k:
                    self.enemy.add(ttank.Tankfac.buildtank())

            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.player.direct = 0
                    self.player.stop(0)
                if event.key == pg.K_RIGHT:
                    self.player.direct = 1
                    self.player.stop(1)
                if event.key == pg.K_DOWN:
                    self.player.direct = 2
                    self.player.stop(2)
                elif event.key == pg.K_LEFT:
                    self.player.direct = 3
                    self.player.stop(3)
    def colliddetect(self):
        a = pg.sprite.groupcollide(self.enemy, self.bltgrp, False, True)
        for i in a:
            self.booms.add(i.boom())
        b = pg.sprite.groupcollide(self.playerg, self.ebltgrp, False, True)
        for i in b:
            self.booms.add(i.boom())
            self.live -= 1
            self.player = ttank.Tank1(self.screen_rect.centerx, self.screen_rect.bottom - 20)
            self.playerg.add(self.player)
    def draw(self):
        self.playerg.draw(self.screen)
        self.enemy.draw(self.screen)
        self.booms.draw(self.screen)
        self.bltgrp.draw(self.screen)
        self.ebltgrp.draw(self.screen)
        self.playerg.update()
        self.enemy.update()
        self.booms.update()
        self.bltgrp.update()
        self.ebltgrp.update()

    def run(self):
        pg.time.set_timer(pg.USEREVENT+1, 500)
        pg.time.set_timer(pg.USEREVENT+2,1500)
        while True:
            if self.live <=0:
                self.gameover()
            self.clock.tick(30)
            self.screen.fill(s.backgroundcolor)
            self.draw()
            self.handleEvent()
            self.colliddetect()
            pg.display.update()
    def gameover(self):
        while True:
            self.screen.fill(s.backgroundcolor)
            go = pg.font.Font(None,50)
            goimage =go.render('GAME OVER',True,(255,255,255))
            go_rect = goimage.get_rect()
            go_rect.center = self.screen_rect.center
            self.screen.blit(goimage,go_rect)
            self.handleEvent()
            pg.display.update()


game = Tankgame()
game.run()
