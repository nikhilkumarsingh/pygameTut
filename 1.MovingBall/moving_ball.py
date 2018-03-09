import pygame

HEIGHT = 600
WIDTH = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving ball")
clock = pygame.time.Clock()

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()
ballrect.center = WIDTH/2, HEIGHT/2
speed = [2, 3]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            quit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > WIDTH:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > HEIGHT:
        speed[1] = -speed[1]

    screen.fill(WHITE)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(FPS)