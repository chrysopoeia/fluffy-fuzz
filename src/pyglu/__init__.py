import pygame

from . import config
from . import event

pygame.init()


class Pyglu(object):
    viewport = None
    components = []
    
    def tick(self):
        for evt in pygame.event.get():
            event.listeners.propagate(evt)
        
        for comp in self.components:
            comp.update()
            self.viewport.blit(*comp.view)
        
        pygame.display.flip()


def init(settings):
    main = Pyglu()
    main.viewport = pygame.display.set_mode((800, 600))
    
    return main
    
    # config_paths = [settings.CONFIG_DEFAULT, os.path.join(settings.CONFIG_DIRECTORY, 'mine.ini')]
    # config_paths = []
    # config.load(config_paths)
