#-------------------------------------------------------------------------------
# Name:        TopLevel.py
# Purpose:     
#
# Author:      Pawel Sznura
#
# Created:     03/12/2020
# Copyright:   (c) Pawel Sznura 2020
#-------------------------------------------------------------------------------

from Match import Match

#add in the pygame imports
import random, sys, copy, os, pygame
from pygame.locals import *

FPS = 30                    # frames per second to update the screen
WINWIDTH = 800              # width of the program's window, in pixels
WINHEIGHT = 800             # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2) #you need to know 1/2 sizes so you can
HALF_WINHEIGHT = int(WINHEIGHT / 2) #place things centrally

# The total width and height of each tile in pixels.
TILEWIDTH = 32
TILEHEIGHT = 32
TILEFLOORHEIGHT = 32

BRIGHTBLUE = (  0, 170, 255)
WHITE      = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

#A dictionary of the images used.  You can then use#floor, wall etc
#in place of the whole pathname

IMAGESDICT = {'floor': pygame.image.load("Images/floor.gif"),
              'wall': pygame.image.load("Images/wall.gif"),
              'snitch': pygame.image.load("Images/snitch.gif"),
              'seeker': pygame.image.load("Images/seeker.gif"),
              'spacer': pygame.image.load("Images/spacer.gif") }

TILEMAPPING = { '#':IMAGESDICT['wall'],
                ' ':IMAGESDICT['floor'],
                '*':IMAGESDICT['snitch'],
                '/':IMAGESDICT['spacer'],
                '!':IMAGESDICT['seeker']}

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Quidditch')
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, BASICFONT



    match = Match()
    while True:
        while True:
            #print(match.draw())
            #print(match.printPoints())

            #thread 1 - look for an action
            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT:
                    # Player clicked the "X" at the corner of the window.
                    terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        match.recognizeInput("L")
                    elif event.key == K_UP:
                        match.recognizeInput("I")
                    elif event.key == K_DOWN:
                        match.recognizeInput("K")
                    elif event.key == K_LEFT:
                        match.recognizeInput("J")
                    # elif event.key == K_SPACE:
                    #     restart()
                    if event.key == K_d:
                        match.recognizeInput("D")
                    elif event.key == K_w:
                        match.recognizeInput("W")
                    elif event.key == K_s:
                        match.recognizeInput("S")
                    elif event.key == K_a:
                        match.recognizeInput("A")
                    else:
                        pass
                mapNeedsRedraw = True

            #thread 2: redraw the screen
            DISPLAYSURF.fill(BGCOLOR) #draws the turquoise background
            #if something has changed, redraw....
            if mapNeedsRedraw:
                #print(str(match.teams[0].seeker.getMovesMade()))
                #print(str(match.teams[1].seeker.getMovesMade()))
                match.update()
                mapSurf = drawMap(match.pitch)
                mapNeedsRedraw = False
            
            mapSurfRect = mapSurf.get_rect()
            mapSurfRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

            # Draw the map on the DISPLAYSURF object.
            DISPLAYSURF.blit(mapSurf, mapSurfRect)

            pygame.display.update() # draw DISPLAYSURF to the screen.
            FPSCLOCK.tick()

            # a = input()
            # match.recognizeInput(a)
            # b = input()
            # match.recognizeInput(b)
            
            # match.update()

            if not match.stillPlaying():
                # before leaving the level print 
                # once more the map and points
                # print(match.draw())
                # print(match.printPoints())
                # input()
                break

        if match.noMoreLevels():
            break

        match.reset()
        #match.update()

    match.gameEnd()

def drawMap(pitch):
    #draw the tile sprites onto this surface.
    #this creates the visual map!
    mapSurfWidth = pitch.getWidth() * TILEWIDTH
    mapSurfHeight = pitch.getLength() * TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR)
    for h in range(pitch.getLength()):
        for w in range(pitch.getWidth()):
            thisTile = pygame.Rect((w * TILEWIDTH, h * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if pitch.getCharAtPos(h, w) in TILEMAPPING:
                #checks in the TILEMAPPING directory above to see if there is a
                #matching picture, then renders it
                baseTile = TILEMAPPING[pitch.getCharAtPos(h,w)]

            # Draw the tiles for the map.
            mapSurf.blit(baseTile, thisTile)
    return mapSurf

def terminate():
    #shutdown routine
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()