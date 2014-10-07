# map + maprendering class
import os, sys, pygame
from logging import debug, info, warn

tile_size = 16

class Map:

    def __init__(self, map_file='data/map.txt'):
        self.width = width
        self.height = height
        pass
        
    def load_map(self):
        # load all assets
        debug('Assets.load_all started')
        surf_cache = {}