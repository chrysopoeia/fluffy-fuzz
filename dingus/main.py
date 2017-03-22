import pygame
import random

from lib import View, BaseController

RESOLUTION = (800, 600)


class TileMap(object):
    def __init__(self, *args, **kwargs):
        self.tiles = self.generate_terrain(10,10)
    
    @staticmethod
    def generate_terrain(w,h):
        return [[{}]*w for x in xrange(0,h)]


class GameController(BaseController):
    def __init__(self, *args, **kwargs):
        super(GameController, self).__init__(*args, **kwargs)
        
        view = View(RESOLUTION)
        
        self.controllers['battlefield'] = BattleController(viewport=view)
        self.views['battlefield'] = view


class BattleController(BaseController):
    def __init__(self, *args, **kwargs):
        super(BattleController, self).__init__(*args, **kwargs)
        
        self.tilemap = TileMap()
        self.entities = pygame.sprite.Group()
        
    def tick(self, events, parent=None):
        super(BattleController, self).tick(events, parent=None)
        
        self.entities.update()
        self.entities.draw(self.viewport)


pygame.init()

viewport = pygame.display.set_mode(RESOLUTION)
scene = GameController(viewport)


while scene:
    events = pygame.event.get()
    
    scene = scene.tick(events)
    
    pygame.display.flip()
