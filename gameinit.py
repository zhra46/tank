import pygame,tank
import setting as s
pygame.init()
screen = pygame.display.set_mode(s.res)
playerTank = tank.Tank(screen)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    playerTank.draw()
    pygame.display.flip()
    playerTank.move('right')


