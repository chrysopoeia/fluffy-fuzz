import pygame
import random

from lib import View, BaseController

RESOLUTION = (800, 600)


class TileMap(object):
    tile_size = (10, 10)
    
    def __init__(self, *args, **kwargs):
        map_size = (10, 10)
        
        self.tiles = self.generate_terrain(*map_size)
        self.image = pygame.surface.Surface((100, 100))
        
        self.render()
    
    @staticmethod
    def generate_terrain(w,h):
        return [[{}]*w for x in xrange(0,h)]
    
    def draw(self, surface):
        return surface.blit(self.image, (0,0))
    
    def render(self):
        surface = self.image
        tiles = self.tiles
        tw,th = self.tile_size
        
        for row_num, row in enumerate(tiles):
            for col_num, col in enumerate(row):
                tile_color = (255, random.randint(0,255), 0)
                tile_rect = (col_num*tw, row_num*th, tw, th)
                
                surface.fill(tile_color, tile_rect)


class GameController(BaseController):
    def __init__(self, *args, **kwargs):
        super(GameController, self).__init__(*args, **kwargs)
        
        view = View(RESOLUTION)
        
        self.controllers['battlefield'] = BattleController(viewport=view)
        self.views['battlefield'] = view


class BattleController(BaseController):
    def __init__(self, *args, **kwargs):
        super(BattleController, self).__init__(*args, **kwargs)
        
        self.background = TileMap()
        self.entities = pygame.sprite.Group()
        
    def tick(self, events, parent=None):
        super(BattleController, self).tick(events, parent=None)
        
        self.background.draw(self.viewport)
        
        self.entities.update()
        self.entities.draw(self.viewport)


pygame.init()

viewport = pygame.display.set_mode(RESOLUTION)
scene = GameController(viewport)


while scene:
    events = pygame.event.get()
    
    scene = scene.tick(events)
    
    pygame.display.flip()
