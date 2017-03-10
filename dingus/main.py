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


# class SceneController(object):
#     fps = 60
    
#     def __init__(self, viewport=None):
#         self.viewport = viewport
#         self.clock = pygame.time.Clock()
#         self.entities = []
#         self.layers = []
#         self.dt = 0
        
#     def handle_events(self):
#         events = pygame.event.get()
        
#     def tick(self):
#         self.dt = self.clock.tick(self.fps)
        
#         self.handle_events()
#         self.update()
#         self.draw(self.viewport)
        
#         pygame.display.flip()
        
#         return self.next
    
#     def update(self):
#         for entity in self.entities:
#             entity.update(self)
    
#     def draw(self, surface):
#         for layer in self.layers:
#             surface.blit(layer.viewport, (12,12))
        
#         for entity in self.entities:
#             surface.blit(entity.viewport, entity.pos)
    
#     @property
#     def next(self):
#         return self


# class Entity(object):
#     pos = [200, 300]
#     radius = 3
    
#     def update(self, scene):
#         self.pos[0] += 1
    
#     def render(self):
#         self.viewport = pygame.Surface((self.radius*2, self.radius*2))
#         self.viewport.set_colorkey((0,0,0))
        
#         pygame.draw.circle(self.viewport, (0,0,255), (self.radius, self.radius), self.radius)


# class GameController(SceneController):
#     def __init__(self, *args, **kwargs):
#         super(GameController, self).__init__(*args, **kwargs)
        
#         tilemap = TileMap()
#         tilemap.render()
        
#         self.layers.append(tilemap)
        
#         e = Entity()
#         e.render()
        
#         self.entities.append(e)


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


class TestController(BaseController):
    def __init__(self, viewport=None):
        super(TestController, self).__init__(viewport=viewport)
        
        v = View(RESOLUTION, name='battlefield')
        battle = BattleController(viewport=v)
        
        self.controllers.append(battle)
        self.views.append(v)



class BattleController(BaseController):
    def __init__(self, viewport=None):
        super(BattleController, self).__init__(viewport=viewport)
        
        tm = TileMap()
        tm.render(self.viewport)


pygame.init()

viewport = pygame.display.set_mode(RESOLUTION)
scene = TestController(viewport)


while scene:
    events = pygame.event.get()
    
    scene = scene.tick(events)
    
    pygame.display.flip()
