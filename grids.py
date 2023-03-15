import pygame
from pygame.locals import *

import hue_table
import saturation_block

pygame.init()

class grid(pygame.sprite.Sprite):  #THIS CLASS OBJECT WORKS AS A CONTAINER FOR THE HUE/SAT VALUES; We inherit from pygame.Sprite so that we can resize grids easily when we resize the window on runtime
    base_color:pygame.Color = pygame.Color('azure4') #azure4
    node: hue_table.hue  # defined for now

    def __init__(self, startX:int, startY:int, width:int, height:int):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.startPos = (startX,startY)  #the topleft coordinates also acts as the index for the grid
        self.color: pygame.color = grid.base_color #DEFAULT COLOR FOR ANY GRID
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect(topleft = self.startPos)
        self.node = None  #declared
        if self.node:
            self.color = self.node.get_color()
        self.image.fill(self.color)

    def insert_node(self, node: hue_table.hue) -> None:
        self.node = node