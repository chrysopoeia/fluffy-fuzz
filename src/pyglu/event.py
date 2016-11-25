class EventListener(object):
    def handle(self, event):
        raise NotImplementedError


class EventListenerRegistry(object):
    def __init__(self):
        self.active_streams = {}
        self.global_listeners = []
    
    def register(self, listener, streams=tuple()):
        if not streams:
            self.global_listeners.append(listener)
        
        for stream_id in streams:
            self.active_streams.setdefault(stream_id, []).append(listener)
    
    def propagate(self, event):
        for listener in self.global_listeners + self.active_streams.get(event.type, []):
            listener.handle(event)


listeners = EventListenerRegistry()


# 0  SDL_NOEVENT
# 1  SDL_ACTIVEEVENT
# 2  SDL_KEYDOWN
# 3  SDL_KEYUP
# 4  SDL_MOUSEMOTION
# 5  SDL_MOUSEBUTTONDOWN
# 6  SDL_MOUSEBUTTONUP
# 7  SDL_JOYAXISMOTION
# 8  SDL_JOYBALLMOTION
# 9  SDL_JOYHATMOTION
# 10  SDL_JOYBUTTONDOWN
# 11  SDL_JOYBUTTONUP
# 12  SDL_QUIT
# 13  SDL_SYSWMEVENT
# 14  SDL_EVENT_RESERVEDA
# 15  SDL_EVENT_RESERVEDB
# 16  SDL_VIDEORESIZE
# 17  SDL_VIDEOEXPOSE
# 18  SDL_EVENT_RESERVED2
# 19  SDL_EVENT_RESERVED3
# 20  SDL_EVENT_RESERVED4
# 21  SDL_EVENT_RESERVED5
# 22  SDL_EVENT_RESERVED6
# 23  SDL_EVENT_RESERVED7
# 24  SDL_USEREVENT
# 32  SDL_NUMEVENTS
