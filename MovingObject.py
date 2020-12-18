# -------------------------------------------------------------------------------
# Name:        movingObject.py
# Version:     1.14
#
# Author:      Pawel Sznura
#
# Created:     03/12/2020
# Copyright:   (c) Pawel Sznura 2020
# -------------------------------------------------------------------------------

class MovingObject:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def getRow(self):
        return self.row

    def setRow(self, newRow):
        self.row = newRow

    def getColumn(self):
        return self.column

    def setColumn(self, newColumn):
        self.column = newColumn

    def move(self, row, column):
        self.setRow(row)
        self.setColumn(column)
