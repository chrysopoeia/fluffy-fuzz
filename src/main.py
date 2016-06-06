import local
import settings
import os
import pygame
import pyglu

pygame.init()

pyglu.init([
    settings.CONFIG_DEFAULT,
    os.path.join(settings.CONFIG_DIRECTORY, 'mine.ini')
])


config = pyglu.config.current
display_dimensions = (config.getint('video', 'width'), config.getint('video', 'height'))

display = pygame.display.set_mode(display_dimensions)
clock = pygame.time.Clock()

pyglu.event.register('sys', pyglu.event.EventListener())


while True:
    dt = clock.tick(60)
    
    pyglu.event.resolve(pygame.event.get())
    pygame.display.flip()
