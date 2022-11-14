import pygame
import sys
from pygame.color import THECOLORS

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((500, 500))  # screen size
pygame.display.set_caption("Snake!")
screen.fill(THECOLORS['black'])  # screen color



# r = pygame.Rect(250, 250, 20, 20)  # size of rect
pygame.draw.rect(screen, 'white', r, 0)  # draw.rect(screen, color, Rect, width)
# pygame.draw.line(screen, (255, 250, 250), [50, 100], [170, 100], 4)  # draw.line(screen, color, Rect, width)
font = pygame.font.SysFont('couriernew', 40)
text = font.render(str("Welcome to the game"), True, THECOLORS['white'])

screen.blit(text, (30, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()