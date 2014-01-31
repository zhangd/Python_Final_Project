'''
"Rainbows and Unicorns"

A deceptively simple, fast-paced, and infinitely upward scrolling platformer.

Angry at someone? Simply replace the unicorn.png with a picture of you, rainbow.png with a picture of the target of your anger, and enjoy wrecking their faces on your journey to the top.

Made by Vardaan Gurung, Matthew Ko, and David Zhang.

'''
import pygame
from random import randint
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
WIDTH = 50
HEIGHT= 50
def new_game(size = 500):
    pygame.init() # initialize all imported pygame modules

    window_size = [size, size] # width, height
    screen = pygame.display.set_mode(window_size)

    pygame.display.set_caption("Rainbows and Unicorns") # caption sets title of Window

    board = Board()

    clock = pygame.time.Clock()
    
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    main_loop(screen, board, clock, background, False)

def update_text(screen, background, message, size = 10):
    textSize = 20
    font = pygame.font.Font(None, 20)
    textY = 0 + textSize
    text = font.render(message, True, (250,250,250), (0,0,0))
    textRect = text.get_rect()
    screen.blit(text, text.get_rect(centerx=background.get_width()/2))
    
def main_loop(screen, board, clock, background, stop):
    score=0
    g=.05
    v=0
    rainbowTimer = 0
    groundPos = screen.get_size()[0]-100
    onGround = True
    board.unicorn.set_y_pos(groundPos-HEIGHT-50)
    x_pos_prev=0 

    pygame.font.init()
    font = pygame.font.Font(None, 36)
    
    while stop == False:
       
        screen.blit(background, (0, 0))
        if pygame.font:
            update_text(screen, background, "Score:" + str(score), size = 10)
        if rainbowTimer % 20 ==0:
            r=Rainbow(4)
            board.addRainbow(r)
        board.unicorn.move_y_pos(1)
        if not onGround:
            groundPos+=1
        for r in board.rainbows:
            if r.disappear_rainbow(board.unicorn.rect):
                v=-3
                board.rainbows.remove(r)
                r.kill()
                score+=1

            r.move_rainbow(-v+3)
        board.rainbows.draw(screen)
        

        events = pygame.event.get()
        if groundPos>400: onGround=False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and onGround:
                v-=5
        pygame.event.pump()
        board.unicorn.move_y_pos(v)
        board.rainbows.draw(screen)
        board.theUnicorn.draw(screen)
        pygame.draw.line(screen, (0,0,0), (0,groundPos), (screen.get_size()[0],groundPos),1)
        if abs(v)>.1:
            groundPos-=v        
        board.unicorn.move_x_pos(pygame.mouse.get_pos()[0])
        x_pos = pygame.mouse.get_pos()[0]
        if(x_pos<x_pos_prev):
           board.unicorn.set_right()
        elif(x_pos>x_pos_prev):
            board.unicorn.set_left()
        pygame.display.flip()
        clock.tick(150)
        if (board.unicorn.get_y_pos()+100>groundPos):
            v=0
            board.unicorn.set_y_pos(groundPos-HEIGHT-50)
        elif v!=0:
            v+=g
        x_pos_prev=x_pos
        rainbowTimer+=1
        pygame.display.flip()
        if board.unicorn.y_pos>500:
            stop=True
        if v>5:v=5
        if v<-5:v=-5
    update_text(screen, background, "GAME OVER", size = 10)
    pygame.display.flip()
    pygame.time.wait(1000)
    print "Your final score was: " + str(score)
 
class Board:
    def __init__(self):
        self.rainbowDict = {}
        self.unicorn = Unicorn(0,400)
        self.rainbows = pygame.sprite.RenderPlain()
        self.theUnicorn = pygame.sprite.RenderPlain()
        self.theUnicorn.add(self.unicorn)
        self.rainbow = Rainbow(4)
    def addRainbow(self, rainbow):
        self.rainbowDict[rainbow.get_current_location()]=rainbow
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
        self.left = self.image
        self.right = pygame.transform.flip(self.image, True, False)
    def get_y_pos(self):
        return self.y_pos
    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)
    def jump(self):
        pass
    def set_y_pos(self, y): #necessary for making sure the unicorn is initiated at ground level
        self.y_pos=y
        self.rect.y=y
    def move_y_pos(self, mouse_y):
        self.y_pos=self.y_pos+mouse_y
        self.rect.y=self.y_pos+mouse_y
    def move_x_pos(self, mouse_x):
        self.x_pos=mouse_x
        self.rect.x=mouse_x
    def set_pic(self):
        self.image = pygame.image.load("unicorn.png").convert_alpha()
    def set_right(self):
        self.image = self.right
    def set_left(self):
        self.image = self.left
        
class Rainbow(pygame.sprite.Sprite):
    def __init__(self, col):
        pygame.sprite.Sprite.__init__(self)
        window_size = 500
        self.a=randint(0,window_size)
        self.b=randint(-500,0)
        self.col = col
        self.rainbow_pic()
        screen = pygame.display.get_surface()
        self.rect = self.image.get_rect()
        self.rect.x = self.a
        self.rect.y = self.b
    def get_current_location(self):
        return (self.a, self.b)

    def rainbow_pic(self):
        self.image = pygame.image.load("rainbow.png").convert_alpha()

    def disappear_rainbow(self, unicorn):
        return self.rect.colliderect(unicorn)

    def move_rainbow(self, x):
        self.b+=x
        self.rect.y = self.b
    
     

new_game()






