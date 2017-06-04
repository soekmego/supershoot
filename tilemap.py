import pygame as py
from settings import *

class Map:
	def __init__(self, filename):
		self.map_data = []
		with open(filename, "rt") as f:
            for line in f:
                self.map_data.append(line)

    self.tilewidth = len(self.data[0])
    self.tileheight = len(self.data)
    self.width = self.tilewidth * TILESIZE
    self.height = self.tileheight * TILESIZE