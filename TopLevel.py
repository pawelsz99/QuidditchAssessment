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
    
    while match.stillPlaying():
        print(match.draw())
        a = input()
        match.recognizeInput(a)
        b = input()
        match.recognizeInput(b)
        
        match.update()
    match.gameEnd()



if __name__ == "__main__":
    main()