import pygame
import random

RESOLUTION = (800, 600)


def generate_map_layout(w,h):
    return [[{}]*w for x in range(0,h)]


class TileMap(object):
    size = (64, 48)
    tile_size = (12, 12)
    
    def __init__(self, size=None):
        w,h = self.size = size or self.size
        tw,th = self.tile_size
        
        self.tiles = generate_map_layout(*self.size)
        self.viewport = pygame.Surface((w*tw,h*th))
        
    def render(self):
        tw,th = self.tile_size
        
        for row_num, row in enumerate(self.tiles):
            for col_num, col in enumerate(row):
                tile_color = (255, random.randint(0,255), 0)
                tile_rect = (col_num*tw, row_num*th, tw, th)
                
                self.viewport.fill(tile_color, tile_rect)


class SceneController(object):
    fps = 60
    
    def __init__(self, viewport=None):
        self.viewport = viewport
        self.clock = pygame.time.Clock()
        self.entities = []
        self.layers = []
        self.dt = 0
        
    def handle_events(self):
        events = pygame.event.get()
        
    def tick(self):
        self.dt = self.clock.tick(self.fps)
        
        self.handle_events()
        self.update()
        self.draw(self.viewport)
        
        pygame.display.flip()
        
        return self.next
    
    def update(self):
        for entity in self.entities:
            entity.update(self)
    
    def draw(self, surface):
        for layer in self.layers:
            surface.blit(layer.viewport, (12,12))
        
        for entity in self.entities:
            surface.blit(entity.viewport, entity.pos)
    
    @property
    def next(self):
        return self


class Entity(object):
    pos = [200, 300]
    radius = 3
    
    def update(self, scene):
        self.pos[0] += 1
    
    def render(self):
        self.viewport = pygame.Surface((self.radius*2, self.radius*2))
        self.viewport.set_colorkey((0,0,0))
        
        pygame.draw.circle(self.viewport, (0,0,255), (self.radius, self.radius), self.radius)


class GameController(SceneController):
    def __init__(self, *args, **kwargs):
        super(GameController, self).__init__(*args, **kwargs)
        
        tilemap = TileMap()
        tilemap.render()
        
        self.layers.append(tilemap)
        
        e = Entity()
        e.render()
        
        self.entities.append(e)


class View(pygame.Surface):
    position = (0,0)
    
    def render(self):
        self.fill((255, 255, 255))


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


pygame.init()

viewport = pygame.display.set_mode(RESOLUTION)

scene = BaseController(viewport)

v = View((200, 200))
v.render()

scene.views.append(v)


while scene:
    events = pygame.event.get()
    
    scene = scene.tick(events)
    
    pygame.display.flip()
