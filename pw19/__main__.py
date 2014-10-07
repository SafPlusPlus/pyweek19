import os, sys, logging, pygame
from logging import debug, info
from assets import Assets

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