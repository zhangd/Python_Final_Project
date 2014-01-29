# THIS IS A MOTHERF***ING COMMENT

import pygame
WIDTH = 50
HEIGHT= 50
def new_game(size = 500):
    pygame.init() # initialize all imported pygame modules

    window_size = [size, size] # width, height
    screen = pygame.display.set_mode(window_size)

    pygame.display.set_caption("Dick In My Ass") # caption sets title of Window

    board = Board()

    clock = pygame.time.Clock()
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    main_loop(screen, board, clock, background, False)
    
def main_loop(screen, board, clock, background, stop):
    g=.1
    v=0
    while stop == False:
        screen.blit(background, (0, 0))
        pygame.event.pump()
        board.rainbows.draw(screen)
        board.theUnicorn.draw(screen)
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                v-=3
                #print(pygame.mouse.get_pos())
        board.unicorn.move_y_pos(v)
         
        #print(pygame.mouse.get_pos()[0])
        board.unicorn.move_x_pos(pygame.mouse.get_pos()[0])
        pygame.display.flip()
        clock.tick(100)
        v+=g
        print(v, board.unicorn.y_pos)
        print("suq madiq")
                                                
class Board:
    def __init__(self):
        self.rainbowDict = {}
        self.unicorn = Unicorn(0,400)
        self.rainbows = pygame.sprite.RenderPlain()
        self.theUnicorn = pygame.sprite.RenderPlain()
        self.theUnicorn.add(self.unicorn)
    def addRainbow(self, rainbow):
        self.rainbowDict[rainbow.getCurrentLocation()]=rainbow
        self.rainbows.add(rainbow)
        
class Unicorn(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = pygame.Surface([WIDTH, HEIGHT]).get_rect()
        self.rect.x=self.x_pos
        self.rect.y=self.y_pos
        self.set_pic()
    def get_y_pos(self):
        return self.y_pos
    def jump(self):
        pass
    def move_y_pos(self, mouse_y):
        self.y_pos=self.y_pos+mouse_y
        self.rect.y=self.y_pos+mouse_y
    def move_x_pos(self, mouse_x):
        self.x_pos=mouse_x
        self.rect.x=mouse_x
    def set_pic(self):
        self.image = pygame.image.load("unicorn.png").convert_alpha()
        #self.image=self.image.get_size(100,100)
      

new_game()
