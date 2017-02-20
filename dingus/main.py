import pygame
import config


def generate_map_layout(w, h):
    return [[{}]*w for x in range(0,h)]


class TileMap(object):
    size = (12, 48)
    tile_size = (24, 24)
    
    def __init__(self, size=None):
        w,h = self.size = size or self.size
        
        tw,th = self.tile_size
        
        self.tiles = generate_map_layout(*self.size)
        self.viewport = pygame.Surface((w*tw,h*th))
        
    def render(self):
        tw, th = self.tile_size
        cobble = pygame.image.load('assets/6903_1.jpg')
        
        for row_num, row in enumerate(self.tiles):
            for col_num, col in enumerate(row):
                self.viewport.blit(cobble, (col_num*tw, row_num*th))
        
    def draw(self, surface):
        surface.blit(self.viewport, (0,0))


class Camera(object):
    fov = (400, 300)
    focus = (0, 0)


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


class GameController(SceneController):
    def __init__(self, *args, **kwargs):
        super(GameController, self).__init__(*args, **kwargs)
        
        self.map = TileMap()
        self.map.render()
        self.map.draw(self.viewport)


pygame.init()

viewport = pygame.display.set_mode(config.RESOLUTION)
scene = GameController(viewport)


while scene:
    scene = scene.tick()
