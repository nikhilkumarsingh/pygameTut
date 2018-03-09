import pygame
import math
from pygame.locals import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 600
HEIGHT = 600
FPS = 60

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Surfer')

ship = pygame.image.load('ship.png')
shiprect = ship.get_rect()

shiprect.x = 100
shiprect.y = 100
speed = 20
degree = 0

left = False
right = False
forward = False
backward = False

while True:

	if right:
		degree -= 2
		while degree < 0:
			degree += 360
	elif left:
		degree += 2
		while degree > 359:
			degree -= 360

	dx = math.cos(math.radians(degree))
	dy = math.sin(math.radians(degree))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			quit()

		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				left = True
			elif event.key == K_RIGHT:
				right = True
			elif event.key == K_UP:
				forward = True
			elif event.key == K_DOWN:
				backward = True

		if event.type == KEYUP:
			left, right, forward, backward = False, False, False, False
			if event.key == K_LEFT:
				left = False
			elif event.key == K_RIGHT:
				right = False
			elif event.key == K_UP:
				forward = False
			elif event.key == K_DOWN:
				backward = False

	if forward:
		shiprect.y -= int(speed * dx)
		shiprect.x -= int(speed * dy)
	elif backward:
		shiprect.y += int(speed * dx)
		shiprect.x += int(speed * dy)


	shiprect.centerx = max(min(shiprect.centerx, WIDTH), 0)
	shiprect.centery = max(min(shiprect.centery, HEIGHT), 0)

	shipR = pygame.transform.rotate(ship, degree)

	screen.fill(BLACK)
	screen.blit(shipR, shiprect)
	pygame.display.update()

	clock.tick(FPS)