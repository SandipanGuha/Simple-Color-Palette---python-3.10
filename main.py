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
        _default_resolution = (400,400)
        _display_handler = pygame.display.set_mode(_default_resolution) #the main surface
        _clock = pygame.time.Clock() #
        _display_handler.fill((0,0,0))
        def update() ->None:
            pygame.display.update()

        _EXIT = False
        while not _EXIT:
            if pygame.event.peek(QUIT):
                _EXIT = True
                pygame.quit()
            update()
    finally:
        sys.quit()
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