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

def main():
    match = Match()
    
    while True:
        print(match.draw())
        print(match.printPoints())
        a = input()
        match.recognizeInput(a)
        b = input()
        match.recognizeInput(b)
        
        match.update()
        # emulating a do-while loop
        if not match.stillPlaying():
            # before leaving the level print 
            # once more the map and points
            print(match.draw())
            print(match.printPoints())
            break
    match.gameEnd()



if __name__ == "__main__":
    main()