# -------------------------------------------------------------------------------
# Name:        Seeker.py
# Purpose:
#
# Author:      Pawel Sznura
#
# Created:     03/12/2020
# Copyright:   (c) Pawel Sznura 2020
# -------------------------------------------------------------------------------

from MovingObject import MovingObject


class Seeker(MovingObject, ):
    def __init__(self, row, column):
        super().__init__(row, column)
        self.movesMade = 0

    def getMovesMade(self):
        return self.movesMade

    def setMovesMade(self, newMoves):
        self.movesMade = newMoves

    def addMovesMade(self):
        self.movesMade += 1
