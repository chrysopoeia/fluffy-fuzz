import pygame
import config
import random


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
    
    def __init__(self, viewport):
        self.viewport = viewport
        self.clock = pygame.time.Clock()
        
    def handle_events(self):
        events = pygame.event.get()
        
    def tick(self):
        dt = self.clock.tick(self.fps)
        
        self.update(dt)
        self.handle_events()
        
        pygame.display.flip()
        
        return self.next
    
    def update(self, dt):
        pass
    
    @property
    def next(self):
        return self


class Entity(object):
    pass


class GameController(SceneController):
    def __init__(self, *args, **kwargs):
        super(GameController, self).__init__(*args, **kwargs)
        
        self.tilemap = TileMap()
        self.tilemap.render()
        
        self.viewport.blit(self.tilemap.viewport, (12,12))


pygame.init()

viewport = pygame.display.set_mode(config.RESOLUTION)
scene = GameController(viewport)


while scene:
    scene = scene.tick()
