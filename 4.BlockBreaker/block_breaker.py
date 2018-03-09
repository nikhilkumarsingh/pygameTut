import pygame
import time
import random

HEIGHT = 800
WIDTH = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(screen, text, x, y, size):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    textSurface, textRect = text_objects(text, font)
    textRect.center  = x, y
    screen.blit(textSurface, textRect)
    pygame.display.update()


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self, speed):
        self.rect.y += speed


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Block breaker")
        self.clock = pygame.time.Clock()
        self.load()


    def load(self):
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.player = Block(WHITE, 20, 20)        


    def init(self):
        self.running = True
        self.block_list.empty()
        self.all_sprites_list.empty()
        self.create_new_blocks(10)
        self.all_sprites_list.add(self.player)
        self.score = 0
        self.speed = 1


    def create_new_blocks(self, num):
        platter = [0, 220, 255]
        for _ in range(num):
            color = (random.choice(platter), random.choice(platter), random.choice(platter))
            block = Block(color, 40, 40)
            block.rect.centerx = random.randrange(WIDTH)
            block.rect.centery = random.randrange(HEIGHT/2)
         
            self.block_list.add(block)
            self.all_sprites_list.add(block)


    def update(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False        

        # update player position
        pos = pygame.mouse.get_pos()
        self.player.rect.centerx = pos[0]
        self.player.rect.centery = pos[1]

        # update blocks position
        self.block_list.update(self.speed)
        
        # check if any block touches ground
        if any(sp.rect.bottom >= HEIGHT for sp in self.block_list.sprites()):
            self.game_over()

        # check player-block collisions
        blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)
        self.create_new_blocks(len(blocks_hit_list))
        self.score += len(blocks_hit_list)

        # increase speed as score increases
        if self.score and self.score%50 ==  0:
            self.speed += 0.05


    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites_list.draw(self.screen)
        message_display(self.screen, "Score: {}".format(self.score), WIDTH/2, 10, 20)
        pygame.display.flip()


    def run(self):
        self.init()
        while self.running:
            self.update()
            self.draw()
            self.clock.tick(FPS)


    def game_over(self):
        message_display(self.screen, "Game over.", WIDTH/2, HEIGHT/2, 40)
        time.sleep(2)
        self.run()


    def __del__(self):
        pygame.quit()


if __name__ == "__main__":
    g = Game()
    g.run()