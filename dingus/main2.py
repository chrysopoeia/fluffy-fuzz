import pygame


def generate_map_layout(w, h):
    return [[{}]*w for x in range(0,h)]


class TileMap(object):
    size = (12, 48)
    
    def __init__(self, size=None):
        self.size = size or self.size
        self.tiles = generate_map_layout(*self.size)


class Camera(object):
    fov = (400, 300)
    focus = (0, 0)


class SceneController(object):
    fps = 60
    
    def __init__(self, viewport):
        self.viewport = viewport
        self.clock = pygame.time.Clock()
        self.camera = Camera()
        self.map = TileMap()
    
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


resolution = (800, 600)
pygame.init()

viewport = pygame.display.set_mode(resolution)
scene = SceneController(viewport)

while scene:
    scene = scene.tick()
