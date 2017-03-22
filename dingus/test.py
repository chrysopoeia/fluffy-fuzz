import pygame
import random

from lib import View, BaseController


RESOLUTION = (800, 600)


def generate_map_layout(w,h):
    return [[{}]*w for x in range(0,h)]


class TileMap(object):
    def __init__(self, size=(64, 48), tile_size=(12, 12)):
        self.size = size
        self.tile_size = tile_size
    
    def render(self, surface):
        tiles = generate_map_layout(*self.size)
        tw,th = self.tile_size
        
        for row_num, row in enumerate(tiles):
            for col_num, col in enumerate(row):
                tile_color = (255, random.randint(0,255), 0)
                tile_rect = (col_num*tw, row_num*th, tw, th)
                
                surface.fill(tile_color, tile_rect)


class Entity(pygame.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Entity, self).__init__(*args, **kwargs)
        
        self.radius = random.randint(1,4)
        
        self.image = pygame.Surface((self.radius*2, self.radius*2))
        self.image.set_colorkey((0,0,0))
        
        self.rect = self.image.get_rect().move(400, 300)
        self.velo = random.randint(1, self.radius)
        
        bc = random.randint(1,200)
        pygame.draw.circle(self.image, (bc, bc, random.randint(bc,255)), (self.radius, self.radius), self.radius)
        
    def update(self, *args, **kwargs):
        minv = -1*self.velo
        
        self.rect = self.rect.move(random.randint(minv, self.velo), random.randint(minv, self.velo))


class GameController(BaseController):
    def __init__(self, *args, **kwargs):
        super(GameController, self).__init__(*args, **kwargs)
        
        view = View(RESOLUTION)
        battle = BattleController(viewport=view)
        
        self.controllers.append(battle)
        self.views.append(view)


class BattleController(BaseController):
    def __init__(self, *args, **kwargs):
        super(BattleController, self).__init__(*args, **kwargs)
        
        tm = TileMap()
        tm.render(self.viewport)
        
        self.entities = pygame.sprite.Group()
        
        for x in xrange(0, 200):
            self.entities.add(Entity())
    
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
