#Python top down shooter made with pygame.
#Still work in progress.

import pygame as pg
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            #check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        #After drawing everything, flip display
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pg.quit()