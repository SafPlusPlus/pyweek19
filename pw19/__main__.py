import os, sys, time, logging, pygame, random

from pygame import Color, Rect
from logging import debug, info
from assets import Assets
from map import Map

random.seed(0) # hurhur

# nicked from http://stackoverflow.com/questions/14058453/making-python-loggers-output-all-messages-to-stdout-in-addition-to-log
root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

class App:

    def __init__(self, name=None):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 480
        self.name = name or 'pw19'
        self.assets = Assets()
        self._map = Map()
        debug('main init done')
 
    def on_init(self):
        debug('on_init started')
        pygame.init()

        self.assets.load_all()
    
        # load icon and set it
        # icon = pygame.image.load(os.path.join('.', 'afuckingbeachballright_icon.png'))
                
        pygame.display.set_icon(self.assets['application_icon'])
        pygame.display.set_caption(self.name)

        self._surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        debug('on_init done')
    
    def test(self):
        debug('test started')
        # just a method in which I test some code :)
        self._surf.fill(Color('white'))
        pygame.draw.rect(self._surf, Color('black') , Rect(9,9,322+16,242), 1)
        pygame.display.flip()
        
        time.sleep(0.1) # I want to see the process... :)
        
        map = self._surf.subsurface(Rect(10,10,320+16,240))
        map.fill(Color('grey'))
        pygame.display.flip()
        
        time.sleep(0.1) # I want to see the process... :)        
        map.blit(self.assets['tile1'], (10,10))
        pygame.display.flip()
        
        time.sleep(0.1) # I want to see the process... :)        
        map.blit(self.assets['tile1'], (-5,-5))     
        map.blit(self.assets['tile1'], (355,235))
        pygame.display.flip()
        
        pool = ['tile1', 'tile2', 'tile3', 'tile4']
        map_height = 32
        map_width = 32
        
        random_map = [[random.choice(pool) for i in xrange(map_width)] for j in xrange(map_height)]        
        random_i = [[random.randint(0,6) for i in xrange(map_width)] for j in xrange(map_height)]        
        scroll_x = 0
        scroll_y = 0        
        for ix in xrange(map_width):
            for iy in xrange(map_height):
                offset_x = ix * 16 + scroll_x
                offset_y = iy * 16 + scroll_y
                map.blit(self.assets[random_map[iy][ix]], (offset_x,offset_y))
                if random_i[iy][ix] == 0:
                    map.blit(self.assets['chair'], (offset_x,offset_y))
        pygame.display.flip()
        
        time.sleep(0.5)
        
        self.map_area = map
        self._map.set_viewport(self.map_area)
        self._map.set_assets(self.assets)
        self._map.generate_random_map()
        self.map_area.fill(Color('white'))
        self._map.render()
        
        
                
                
        
        
        
        debug('test done')
        
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._quit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == u'q' and (pygame.KMOD_META & event.mod):
                self._quit()

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        self.test()

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
        
    def _quit(self):
        # quit + optional cleanup?
        debug('Quitting...')
        self._running = False
        

def main():
    """ your app starts here
    """
    theApp = App()
    debug('starting main app')
    theApp.on_execute()