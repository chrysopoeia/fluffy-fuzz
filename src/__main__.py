import pygame
import settings
import pyglu


class UserStats(object):
    surface = None
    
    def __init__(self):
        self.surface = pygame.Surface((200, 200))
        
        pyglu.event.listeners.register(self.handle_update_stats, (4,))
    
    def update(self):
        self.render()
    
    def handle_update_stats(self, evt):
        print evt, 'wooot'
    
    def render(self):
        self.surface.fill((255,0,0))
    
    @property
    def view(self):
        return (self.surface, (0,0))


if __name__ == '__main__':
    main = pyglu.init(settings)
    main.components.append(UserStats())
    
    while True:
        main.tick()



# import os
# import pygame
# import pyglu

# from constants import *


# pygame.init()
# pyglu.init([CONFIG_DEFAULT, os.path.join(CONFIG_DIRECTORY, 'mine.ini')])

# config = pyglu.config.current
# display_dimensions = (config.getint('video', 'width'), config.getint('video', 'height'))

# display = pygame.display.set_mode(display_dimensions)
# clock = pygame.time.Clock()


# class SomeHandler(pyglu.event.EventListener):
#     def handle(self, event):
#         print event

# pyglu.event.listeners.register(SomeHandler(), (2,3))


# while True:
#     dt = clock.tick(60)
    
#     for event in pygame.event.get():
#         pyglu.event.listeners.propagate(event)
    
#     pygame.event.get()
#     pygame.display.flip()
