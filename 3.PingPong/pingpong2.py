import pygame
import time

HEIGHT = 600
WIDTH = 600
FPS = 80

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(screen, text, x, y, size):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    textSurface, textRect = text_objects(text, font)
    textRect.center  = x, y
    screen.blit(textSurface, textRect)
    pygame.display.update()


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ping Pong")
        self.clock = pygame.time.Clock()
        self.load()

    def run(self):
        self.init()

        while self.running:
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def load(self):
        self.collision_sound = pygame.mixer.Sound("collision.wav")
        self.ball = pygame.image.load("ball.png")
        self.ballrect = self.ball.get_rect()
        self.paddle = pygame.Rect((0, HEIGHT/2), (30, 150))

    def init(self):
        self.running = True
        self.ballrect.center = WIDTH/2, HEIGHT/2
        self.ball_speed = [5,7]
        self.paddle.centery = HEIGHT/2
        self.paddle_speed = 0
        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0


    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.paddle_speed = -5
                elif event.key == pygame.K_DOWN:
                    self.paddle_speed = 5
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    self.paddle_speed = 0

        self.paddle.y += self.paddle_speed
        self.paddle.bottom = max(min(self.paddle.bottom, HEIGHT), self.paddle.height)

        self.ballrect = self.ballrect.move(self.ball_speed)

        if self.paddle.colliderect(self.ballrect) or self.ballrect.right > WIDTH:
            self.ball_speed[0] = -self.ball_speed[0]
            pygame.mixer.Sound.play(self.collision_sound)

        elif self.ballrect.top < 0 or self.ballrect.bottom > HEIGHT:
            self.ball_speed[1] = -self.ball_speed[1]
            pygame.mixer.Sound.play(self.collision_sound)

        elif self.ballrect.left < 0:
            self.game_over()

        self.elapsed_time = int((pygame.time.get_ticks() - self.start_time)/1000)

        if self.elapsed_time%10 == 5:
            self.ball_speed[0] *= 1.01
            self.ball_speed[1] *= 1.01


    def draw(self):
        self.screen.fill(GREEN)
        self.screen.blit(self.ball, self.ballrect)
        pygame.draw.rect(self.screen, BLACK, self.paddle)
        message_display(self.screen, "Score: {}".format(self.elapsed_time), WIDTH/2, 10, 20)
        pygame.display.flip()


    def game_over(self):
        message_display(self.screen, "Game over.", WIDTH/2, HEIGHT/2, 40)
        time.sleep(2)
        self.run()

    def __del__(self):
        pygame.quit()


if __name__ == "__main__":
    g = Game()
    g.run()