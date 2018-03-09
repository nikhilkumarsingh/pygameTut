import pygame
import time


HEIGHT = 600
WIDTH = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = None
clock = None
running = True

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
paddle = pygame.Rect((0, HEIGHT/2), (30, 150))
ball_speed = [5,7]
paddle_speed = 0


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def message_display(text, x, y, size):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    textSurface, textRect = text_objects(text, font)
    textRect.center  = x, y
    screen.blit(textSurface, textRect)
    pygame.display.update()


def game_over():
    message_display("Game over.", WIDTH/2, HEIGHT/2, 40)
    time.sleep(2)
    game_loop()


def init():
    global screen, clock, running, paddle, ballrect, ball_speed, paddle_speed
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving ball")
    clock = pygame.time.Clock()
    running = True
    """
    complete it!
    """

def update():
    global paddle, ballrect, paddle_speed, ball_speed, running
    """
    complete event list
    """

    """
    update paddle position
    """

    """
    update ball position
    """

    """
    check ball paddle collision
    """

def draw():
    global ball, ballrect, paddle, screen
    screen.fill(GREEN)
    """
    draw ball and paddle
    """
    pygame.display.flip()


def game_loop():
    pygame.init()
    init()
    
    while running:
        update()
        draw()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()