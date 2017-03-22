from collections import OrderedDict
from pygame import Surface


class View(Surface):
    def __init__(self, size, position=(0,0)):
        super(View, self).__init__(size)
        
        self.rect = self.get_rect().move(position)


class BaseController(object):
    def __init__(self, viewport=None):
        self.viewport = viewport
        self.views = OrderedDict()
        self.controllers = OrderedDict()
    
    def tick(self, events, parent=None):
        for name, controller in self.controllers.items():
            controller.tick(events, self)
        
        for name, view in self.views.items():
            self.viewport.blit(view, view.rect)
        
        return self
