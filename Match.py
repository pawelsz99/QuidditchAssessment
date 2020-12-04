# -------------------------------------------------------------------------------
# Name:        Match.py
# Purpose:
#
# Author:      Pawel Sznura
#
# Created:     03/12/2020
# Copyright:   (c) Pawel Sznura 2020
# -------------------------------------------------------------------------------

from Pitch import Pitch
from GoldenSnitch import GoldenSnitch
from Team import Team


class Match():
    def __init__(self):
        self.pith = Pitch()  # 20x10
        self.teams = [Team("A"), Team("B")]
        # placing seekers to starting positions
        self.teams[0].seeker.setRow(1)
        self.teams[0].seeker.setColumn(1)
        self.teams[1].seeker.setRow(18)
        self.teams[1].seeker.setColumn(1)
        # and snitch in the middle
        self.goldenSnitch = GoldenSnitch(10, 4)
        self.points = [0, 0]
        self.charDict = {
            "seeker": "!",
            "goldenSnitch": "*",
            "border": "#",
            "emptySpace": " "
        }
        self.updatePitch(self.pith, self.teams, self.goldenSnitch)

    def gameEnd(self):
        print("game ends")
        # TODO

    def stillPlaying(self):
        if self.goldenSnitch.isFree():
            return True
        else:
            return False

    def update(self):
        self.updatePitch(self.pith, self.teams, self.goldenSnitch)

    def updatePitch(self, pitch, teams, goldenSnitch):
        # remember to clear the positions before placing new chars
        pitch.placeOnPitch(
            self.charDict["seeker"], teams[0].seeker.getRow(), teams[0].seeker.getColumn())
        pitch.placeOnPitch(
            self.charDict["seeker"], teams[1].seeker.getRow(), teams[1].seeker.getColumn())
        pitch.placeOnPitch(
            self.charDict["goldenSnitch"], goldenSnitch.getRow(), goldenSnitch.getColumn())

    def draw(self):
        return str(self.pith)

    def newPosition(self, seeker, newRow, newColumn):
        if self.pith.isPositionFree(newRow, newColumn):
            seeker.move(newRow, newColumn)
            return True
        else:
            print("cant move")
            return False

    def recognizeInput(self, char):
        char = char.upper()
        if char == "A":
            # seeker1 left
            seeker = self.teams[0].seeker
            if self.newPosition(seeker, seeker.getRow(), seeker.getColumn()-1):
                self.pith.clearPosition(seeker.getRow(), seeker.getColumn()+1)
        elif char == "D":
            # seeker1 right
            seeker = self.teams[0].seeker
            if self.newPosition(seeker, seeker.getRow(), seeker.getColumn()+1):
                self.pith.clearPosition(seeker.getRow(), seeker.getColumn()-1)
        elif char == "W":
            # seeker1 up
            seeker = self.teams[0].seeker
            if self.newPosition(seeker, seeker.getRow()-1, seeker.getColumn()):
                self.pith.clearPosition(seeker.getRow()+1, seeker.getColumn())
        elif char == "S":
            # seeker1 down
            seeker = self.teams[0].seeker
            if self.newPosition(seeker, seeker.getRow()+1, seeker.getColumn()):
                self.pith.clearPosition(seeker.getRow()-1, seeker.getColumn())
        elif char == "J":
            # seeker2 left
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow(), seeker.getColumn()-1):
                self.pith.clearPosition(seeker.getRow(), seeker.getColumn()+1)
        elif char == "L":
            # seeker2 right
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow(), seeker.getColumn()+1):
                self.pith.clearPosition(seeker.getRow(), seeker.getColumn()-1)
        elif char == "I":
            # seeker2 up
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow()-1, seeker.getColumn()):
                self.pith.clearPosition(seeker.getRow()+1, seeker.getColumn())
        elif char == "K":
            # seeker2 down
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow()+1, seeker.getColumn()):
                self.pith.clearPosition(seeker.getRow()-1, seeker.getColumn())
        else:
            print("input fail")
