import pygame
class Eventdetect(object):
    def keydetect(self,tank=None):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tank.move('up')
                    print (tank.rect.x)