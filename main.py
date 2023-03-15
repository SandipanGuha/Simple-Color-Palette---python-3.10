import random

import grids
import hue_table

if __name__ == '__main__':
    try:
        ''' ***********************************^^^^^ ALL IMPORTS WILL BE DONE HERE  ^^^^^***********************************'''
        import pygame
        import sys
        import os
        from pygame.locals import *

        pygame.init() # INITIALIZES PYGAME
    except ModuleNotFoundError as ModuleNotFoundError:
        print("Error:",ModuleNotFoundError)
        pass
    else:
        ''' ***************************^^^^^ THE CORE MECHANICS WILL BE IMPLEMENTED AND RUN FROM HERE ^^^^^************************************'''
        _default_resolution = (400,500) # SECTION A + SECTION B
        _section_A = pygame.Surface([400,400])
        _section_B = pygame.Surface([400,100])
        _display_handler = pygame.display.set_mode(_default_resolution) #the main surface
        _clock = pygame.time.Clock() #
        _display_handler.fill((0,0,0))
        _EXIT = False

        def update_display() -> None:
            pygame.display.update()

        def define_grids() -> None:
            _grids = pygame.sprite.Group()    #Empty group which will hold all the GRID sprites
            blockSize = 20  # Set the size of the grid block
            WINDOW_WIDTH,WINDOW_HEIGHT = _section_A.get_width(),_section_A.get_height()
            _table = [[grids.grid] *  WINDOW_HEIGHT] * WINDOW_WIDTH
            for x in range(0, WINDOW_WIDTH, blockSize):
                for y in range(0, WINDOW_HEIGHT, blockSize):
                    _grid = grids.grid(x, y, blockSize, blockSize)
                    _table[x][y]=_grid
                    #_display_handler.blit(_grid.image, _grid.rect)
                    _grids.add(_grid)
            return _grids, _table
        def draw_sprite_group( group: pygame.sprite.Group, surface:pygame.Surface) -> None:
            group.draw(surface)


        _grids,_grid_table = define_grids()  #called once; created a grid group
        for i in range(301,_section_A.get_width()):
            for j in range(0,_section_A.get_height()):
                _grid_table[i][j].insert_node(hue_table.hue((random.randint(0,255),random.randint(0,255),random.randint(0,255))))


        ''' *****************************************^^^^^^^^^ [ MAIN LOOP ] ^^^^^^^^*********************************************'''
        while not _EXIT:
            if pygame.event.peek(QUIT):
                _EXIT = True
            draw_sprite_group(_grids,_section_A)
            _display_handler.blit(_section_A, (0, 0))  # bliting SECTION A
            _display_handler.blit(_section_B, (0, 400))  # bliting SECTION B
            update_display()
    finally:
        pygame.quit()
        #TODO GARBAGE COLLECTION
            # import pygame
        # from pygame.locals import *
        #
        # pygame.init() # INITIALIZES PYGAME
        # ''' ***************************^^^^^ THE CORE MECHANICS WILL BE IMPLEMENTED AND RUN FROM HERE ^^^^^************************************'''
        # _default_resolution = (400,400)
        # _display_handler = pygame.display.set_mode(_default_resolution) #the main surface
        # _clock = pygame.time.Clock() #
        # _display_handler.fill((0,0,0))
        # def update() ->None:
        #     pygame.display.update()
        #
        # _EXIT = False
        # while not _EXIT:
        #     if pygame.event.peek(QUIT):
        #         _EXIT = True
        #         pygame.quit()
        #     update()