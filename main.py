import pygame
import config
import sys

pygame.init()

config.load('mine.cfg')
cfg = config.current

display_width = cfg.getint('video', 'width')
display_height = cfg.getint('video', 'height')

display = pygame.display.set_mode((display_width, display_height), pygame.OPENGL)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.flip()
