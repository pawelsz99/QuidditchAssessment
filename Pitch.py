#-------------------------------------------------------------------------------
# Name:        Pitch.py
# Version:     1.12
#
# Author:      Pawel Sznura
#
# Created:     03/12/2020
# Copyright:   (c) Pawel Sznura 2020
#-------------------------------------------------------------------------------

class Pitch:
    def __init__(self):
        self.width = 10
        self.length = 20
        self.listOfLevels = [[['#','#','#','#','#','#','#','#','#','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#','#','#','#','#','#','#','#','#','#']],

                     [['#','#','#','#','#','#','#','#','#','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ','#','#','#','#','#','#',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ','#','#','#','#',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ','#','#',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ','#','#',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ','#','#','#','#',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ','#','#','#','#','#','#',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#','#','#','#','#','#','#','#','#','#']]]
        self.mapOfPitch = self.listOfLevels[0]

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getLength(self):
        return self.length

    def setLength(self, newLength):
        self.length = newLength

    def setLevel(self, level):
        self.mapOfPitch = self.listOfLevels[level]

    def getMaxLevel(self):
        """Returns:
            int: the postinion of the last level in listOfLevels
        """
        return len(self.listOfLevels) - 1

    def placeOnPitch(self, char, row, column):
        self.mapOfPitch[row][column] = char

    def __str__(self):
        printMe = ""
        for i in range(0, self.length):
            for j in self.mapOfPitch[i]:
                printMe += j
            printMe += "\n"
        return printMe

    def isPlayerOnPosition(self, row, column):
        position = self.mapOfPitch[row][column]
        if position == "!":
            return True
        else:
            return False

    def isPositionFree(self, row, column):
        position = self.mapOfPitch[row][column]
        if position == " " or position == "*":
            return True
        else:
            return False

    def clearPosition(self, row, column):
        self.mapOfPitch[row][column] = " "

    def getCharAtPos(self, row, col):
        return self.mapOfPitch[row][col]
