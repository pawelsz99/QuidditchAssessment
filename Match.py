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
        self.pitch = Pitch()  # 20x10
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
        self.updatePitch()

    def gameEnd(self):
        print("game ends")
        # TODO

    def stillPlaying(self):
        if self.goldenSnitch.isFree():
            return True
        else:
            return False

    def awardPoints(self, team):
        team.addPoints(150)

    def update(self):
        self.checkSnitch()
        self.updatePitch()

    def checkSnitch(self):
        snitch = self.goldenSnitch
        seeker1 = self.teams[0].seeker
        seeker2 = self.teams[1].seeker

        if snitch.getRow() == seeker1.getRow() and snitch.getColumn() == seeker1.getColumn():
            print("Snitch captured by team 1 ")
            self.awardPoints(self.teams[0])
            snitch.captured()
        elif snitch.getRow() == seeker2.getRow() and snitch.getColumn() == seeker2.getColumn():
            print("Snitch captured by team 2 ")
            self.awardPoints(self.teams[1])
            snitch.captured()

    def updatePitch(self):
        self.pitch.placeOnPitch(
            self.charDict["seeker"], self.teams[0].seeker.getRow(), self.teams[0].seeker.getColumn())
        self.pitch.placeOnPitch(
            self.charDict["seeker"], self.teams[1].seeker.getRow(), self.teams[1].seeker.getColumn())
        if self.goldenSnitch.isFree():
            self.pitch.placeOnPitch(
                self.charDict["goldenSnitch"], self.goldenSnitch.getRow(), self.goldenSnitch.getColumn())

    def draw(self):
        return str(self.pitch)

    def printPoints(self):
        printMe = "Team " + self.teams[0].name + \
            " " + str(self.teams[0].getPoints())
        printMe += " : " + \
            str(self.teams[1].getPoints()) + " Team " + self.teams[1].name
        return printMe

    def newPosition(self, seeker, newRow, newColumn):
        if self.pitch.isPositionFree(newRow, newColumn):
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
                self.pitch.clearPosition(seeker.getRow(), seeker.getColumn()+1)
        elif char == "D":
            # seeker1 right
            seeker = self.teams[0].seeker
            if self.newPosition(seeker, seeker.getRow(), seeker.getColumn()+1):
                self.pitch.clearPosition(seeker.getRow(), seeker.getColumn()-1)
        elif char == "W":
            # seeker1 up
            seeker = self.teams[0].seeker
            if self.newPosition(seeker, seeker.getRow()-1, seeker.getColumn()):
                self.pitch.clearPosition(seeker.getRow()+1, seeker.getColumn())
        elif char == "S":
            # seeker1 down
            seeker = self.teams[0].seeker
            if self.newPosition(seeker, seeker.getRow()+1, seeker.getColumn()):
                self.pitch.clearPosition(seeker.getRow()-1, seeker.getColumn())
        elif char == "J":
            # seeker2 left
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow(), seeker.getColumn()-1):
                self.pitch.clearPosition(seeker.getRow(), seeker.getColumn()+1)
        elif char == "L":
            # seeker2 right
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow(), seeker.getColumn()+1):
                self.pitch.clearPosition(seeker.getRow(), seeker.getColumn()-1)
        elif char == "I":
            # seeker2 up
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow()-1, seeker.getColumn()):
                self.pitch.clearPosition(seeker.getRow()+1, seeker.getColumn())
        elif char == "K":
            # seeker2 down
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow()+1, seeker.getColumn()):
                self.pitch.clearPosition(seeker.getRow()-1, seeker.getColumn())
        else:
            print("input fail")
