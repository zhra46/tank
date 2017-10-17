import pygame,setting
class Tank(object):
    def __init__(self,screen):
        try:
            self.tank = pygame.image.load('tank-images/tankU.gif')
        except pygame.error:
            print('wrong path or filename')
            pygame.quit()
            quit()
        self.rect = self.tank.get_rect()

        self.rect.midbottom = screen.get_rect().midbottom
        self.screen = screen
    def move(self,direct):
        if direct == 'up':
            self.tank = pygame.image.load('tank-images/tankU.gif')
            self.rect=self.rect.move(0,-setting.tank_move_speed)
        if direct == 'down':
            self.tank = pygame.image.load('tank-images/tankD.gif')
            self.rect=self.rect.move(0,setting.tank_move_speed)
        if direct == 'left':
            self.tank = pygame.image.load('tank-images/tankL.gif')
            self.rect=self.rect.move(-setting.tank_move_speed,0)
        if direct == 'right':
            self.tank = pygame.image.load('tank-images/tankR.gif')
            self.rect=self.rect = self.rect.move(setting.tank_move_speed,0)
    def draw(self,):
        self.screen.blit(self.tank,self.rect)
        #print('test draw')
