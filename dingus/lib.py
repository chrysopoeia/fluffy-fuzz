from pygame import Surface


class View(Surface):
    def __init__(self, size, position=(0,0), name=None):
        super(View, self).__init__(size)
        
        self.rect = self.get_rect().move(position)
        self.name = name


class BaseController(object):
    def __init__(self, viewport=None):
        self.viewport = viewport
        self.views = []
        self.controllers = []
    
    def tick(self, events, parent=None):
        for controller in self.controllers:
            controller.tick(events, self)
        
        for view in self.views:
            self.viewport.blit(view, view.rect)
        
        return self
