# asset class
import os, sys, pygame
from logging import debug, info, warn

tile_size = 16

class Assets:

    def __init__(self, data_dir='data', data_file='data/assets.txt'):
        self.data_dir = data_dir
        self.data_file = data_file
        self.assets = {}
        
    def load_all(self):
        # load all assets
        debug('Assets.load_all started')
        surf_cache = {}
        
        with open(self.data_file, 'r') as index_file:
            for line_no, line in enumerate(index_file.readlines()):
                line = line.strip()
                debug(line)
                if line.startswith('#'): continue
                # Floor.png, tile1, 1, 4
                try:
                    fn, id, ix, iy = (s.strip() for s in line.split(','))
                    if fn not in surf_cache:
                        surf_cache[fn] = pygame.image.load(os.path.join(self.data_dir, fn))
                        debug('loaded %s into loading cache' % fn)
                    self.assets[id] = surf_cache[fn].subsurface(Rect(ix*tile_size, iy*tile_size, tile_size, tile_size))
                    debug('loaded %s as subsurface' % id)
                    
                except ValueError:
                    warn('ValueError when loading line %d in the %s' % (line_no + 1, self.data_file))
                    
                
        
        debug('Assets.load_all done')
    