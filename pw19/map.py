# map + maprendering class
import os, sys, pygame, random
from logging import debug, info, warn

tile_size = 16

class Map:

    def __init__(self, map_file='data/map.txt', viewport=None):
        self._viewport = viewport
        self._scroll_x = 3
        self._scroll_y = 3
        
    def generate_random_map(self):
        self._width = random.randint(16,32)
        self._height = random.randint(16,32)
        
        self._scroll_x = (self._width * tile_size) // 2
        self._scroll_y = (self._height * tile_size) // 2
        
        pool = ['tile1', 'tile2', 'tile3', 'tile4', 'wall1']
        
        self._tiles = [[random.choice(pool) for i in xrange(self._width)] for j in xrange(self._height)]        
        random_i = [[random.randint(0,6) for i in xrange(self._width)] for j in xrange(self._height)]  
    
    def set_viewport(self, viewport):
        self._viewport = viewport
        
    def set_assets(self, assets):
        self._assets = assets
        
    def load_map(self):
        # load all assets
        debug('Assets.load_all started')
        surf_cache = {}
        
    def render(self):
        offset_x = -self._scroll_x + (self._viewport.get_width() - tile_size) // 2
        offset_y = -self._scroll_y + (self._viewport.get_height() - tile_size) // 2
        debug('offset = %d, %d' % (offset_x, offset_y))
     
        for ix in xrange(self._width):
            for iy in xrange(self._height):
                dx = ix * tile_size + offset_x
                dy = iy * tile_size + offset_y
                self._viewport.blit(self._assets[self._tiles[iy][ix]], (dx,dy))
                #if random_i[iy][ix] == 0:
                #    self._viewport.blit(self.assets['chair'], (dx,dy))
        pygame.draw.circle(self._viewport, (0,0,0), (160,120), 16, 3)    
            
        pygame.display.flip()
        