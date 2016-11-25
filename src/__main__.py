import os
import pygame
import pyglu

from constants import *


pygame.init()
pyglu.init([CONFIG_DEFAULT, os.path.join(CONFIG_DIRECTORY, 'mine.ini')])

config = pyglu.config.current
display_dimensions = (config.getint('video', 'width'), config.getint('video', 'height'))

display = pygame.display.set_mode(display_dimensions)
clock = pygame.time.Clock()


class SomeHandler(pyglu.event.EventListener):
    def handle(self, event):
        print event

pyglu.event.listeners.register(SomeHandler(), (2,3))


while True:
    dt = clock.tick(60)
    
    for event in pygame.event.get():
        pyglu.event.listeners.propagate(event)
    
    pygame.event.get()
    pygame.display.flip()
