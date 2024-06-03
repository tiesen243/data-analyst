                                                                     
                                                                     
                                                                     
                                             
# Kimberly Todd
# CSE 142 Autumn 2008

# Whack-a-mole game using pygame

from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000;

class Mole(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("mole.gif").convert()
        self.rect = self.image.get_rect()

    # move mole to a new random location
    # after it is hit
    def flee(self):
        randX = randint(0, 600)
        randY = randint(0, 400)
        self.rect.center = (randX,randY)

class Shovel(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("shovel.gif").convert()
        self.rect = self.image.get_rect()

    # did the shovel hit the mole?
    def hit(self, target):
        return self.rect.colliderect(target)

    # follows the mouse cursor
    def update(self):
        self.rect.center = mouse.get_pos()


#main
init()

screen = display.set_mode((640, 480))
display.set_caption('Whack-a-mole')

# hide the mouse cursor
mouse.set_visible(False)

f = font.Font(None, 25)

# create the mole and shovel
mole = Mole()
shovel = Shovel()
# creates a group of sprites so all can be updated at once
sprites = RenderPlain(mole, shovel)

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

# loop until user quits
while True:
    e = event.poll()
    if e.type == QUIT:
        quit()
        break
    elif e.type == MOUSEBUTTONDOWN:
        if shovel.hit(mole):
            mixer.Sound("hit.wav").play()
            mole.flee()
            hits += 1

            # reset timer
            time.set_timer(USEREVENT + 1, DELAY)
            
    elif e.type == USEREVENT + 1: # TIME has passed
        mole.flee()

    # cover everything in white so that we can paint sprites in new locations
    screen.fill(Color("white"))
    t = f.render("Hits = " + str(hits), False, (0,0,0))
    screen.blit(t, (320, 0)) # draw text to screen

    # update and redraw sprites
    sprites.update()
    sprites.draw(screen)
    display.update()
