import pygame
import random

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
        
        self.radius = random.randint(1,8)
        self.image = pygame.Surface((self.radius*2, self.radius*2))
        self.image.set_colorkey((0,0,0))
        
        self.rect = self.image.get_rect().move(400, 300)
        self.velo = random.randint(1,4)
        
        c = random.randint(1,200)
        pygame.draw.circle(self.image, (c, c, random.randint(c,255)), (self.radius, self.radius), self.radius)
        
    def update(self, *args, **kwargs):
        self.rect = self.rect.move(random.randint(-1*self.velo,self.velo), random.randint(-1*self.velo,self.velo))


class View(pygame.Surface):
    def __init__(self, size, position=(0,0), name=None):
        super(View, self).__init__(size)
        
        self.name = name
        self.position = position


class BaseController(object):
    def __init__(self, viewport=None):
        self.viewport = viewport
        self.views = []
        self.controllers = []
    
    def tick(self, events, parent=None):
        for controller in self.controllers:
            controller.tick(events, self)
        
        for view in self.views:
            self.viewport.blit(view, view.position)
        
        return self


class GameController(BaseController):
    def __init__(self, viewport=None):
        super(GameController, self).__init__(viewport=viewport)
        
        v = View(RESOLUTION, name='battlefield')
        battle = BattleController(viewport=v)
        
        self.controllers.append(battle)
        self.views.append(v)



class BattleController(BaseController):
    def __init__(self, viewport=None):
        super(BattleController, self).__init__(viewport=viewport)
        
        tm = TileMap()
        tm.render(self.viewport)
        
        self.g = pygame.sprite.Group()
        
        for x in xrange(0, 200):
            self.g.add(Entity())
    
    def tick(self, events, parent=None):
        super(BattleController, self).tick(events, parent=None)
        
        self.g.update()
        self.g.draw(self.viewport)


pygame.init()

viewport = pygame.display.set_mode(RESOLUTION)
scene = GameController(viewport)


while scene:
    events = pygame.event.get()
    
    scene = scene.tick(events)
    
    pygame.display.flip()
