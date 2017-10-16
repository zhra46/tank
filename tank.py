import pygame,setting
class Tank(object):
    def __init__(self,screen):
        self.tank = pygame.image.load('src/tank.png')
        self.rect = self.tank.get_rect()

        self.rect.midbottom = screen.get_rect().midbottom
        self.screen = screen
    def move(self,direct):
        if direct == 'up':
            self.rect.move(0,-setting.tank_move_speed)
        if direct == 'down':
            self.rect.move(0,setting.tank_move_speed)
        if direct == 'left':
            self.rect.move(-setting.tank_move_speed,0)
        if direct == 'right':
            self.rect = self.rect.move(setting.tank_move_speed,0)
    def draw(self,):
        self.screen.blit(self.tank,self.rect)

