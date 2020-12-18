# -------------------------------------------------------------------------------
# Name:        Team.py
# Version:     1.14
#
# Author:      Pawel Sznura
#
# Created:     03/12/2020
# Copyright:   (c) Pawel Sznura 2020
# -------------------------------------------------------------------------------

from Seeker import Seeker


class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.seeker = Seeker(0, 0)

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getPoints(self):
        return self.points

    def setPoints(self, newPoints):
        self.points = newPoints

    def addPoints(self, addedPoints):
        self.points += addedPoints
