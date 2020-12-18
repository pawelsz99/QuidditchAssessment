# -------------------------------------------------------------------------------
# Name:        Match.py
# Version:     1.14
#
# Author:      Pawel Sznura
#
# Created:     03/12/2020
# Copyright:   (c) Pawel Sznura 2020
# -------------------------------------------------------------------------------

from Pitch import Pitch
from GoldenSnitch import GoldenSnitch
from Team import Team
import random


class Match():
    def __init__(self):
        self.pitch = Pitch()  # 20x10
        self.teams = [Team("A"), Team("B")]
        # set the starting coordinates
        self.teams[0].seeker.setRow(1)
        self.teams[0].seeker.setColumn(1)
        self.teams[1].seeker.setRow(18)
        self.teams[1].seeker.setColumn(1)
        self.goldenSnitch = GoldenSnitch(10, 4)
        self.points = [0, 0]
        self.charDict = {
            "seeker": "!",
            "goldenSnitch": "*",
            "border": "#",
            "emptySpace": " "
        }
        self.level = 0
        # place seeker and snitch on pitch
        self.updatePitchSeekers()
        self.updatePitchSnitch()

    def reset(self):
        # new map level
        self.newLevel()
        # set the starting coordinates
        self.teams[0].seeker.setRow(1)
        self.teams[0].seeker.setColumn(1)
        self.teams[1].seeker.setRow(18)
        self.teams[1].seeker.setColumn(1)
        self.goldenSnitch = GoldenSnitch(10, 4)
        # reset the counter for moves made
        self.teams[0].seeker.setMovesMade(0)
        self.teams[1].seeker.setMovesMade(0)

    def newLevel(self):
        maxLevel = self.pitch.getMaxLevel()
        if self.level < maxLevel:
            self.level += 1
            self.pitch.setLevel(self.level)
        else:
            print("Error no more levels")

    def noMoreLevels(self):
        if self.level == self.pitch.getMaxLevel():
            return True
        else:
            return False

    def stillPlaying(self):
        if self.goldenSnitch.isFree():
            return True
        else:
            return False

    def awardPoints(self, team):
        team.addPoints(150)

    def moveSnitch(self):
        snitch = self.goldenSnitch
        if self.level > 0 and snitch.isFree():
            # if player next to then run away
            # check left
            if self.pitch.isPlayerOnPosition(snitch.getRow(), snitch.getColumn()-1):
                # run away, right
                if self.newPosition(snitch, snitch.getRow(), snitch.getColumn()+1):
                    self.pitch.clearPosition(
                        snitch.getRow(), snitch.getColumn()-1)
            # check right
            elif self.pitch.isPlayerOnPosition(snitch.getRow(), snitch.getColumn()+1):
                # run away, left
                if self.newPosition(snitch, snitch.getRow(), snitch.getColumn()-1):
                    self.pitch.clearPosition(
                        snitch.getRow(), snitch.getColumn()+1)
            # check up
            elif self.pitch.isPlayerOnPosition(snitch.getRow()-1, snitch.getColumn()):
                # run away, down
                if self.newPosition(snitch, snitch.getRow()+1, snitch.getColumn()):
                    self.pitch.clearPosition(
                        snitch.getRow()-1, snitch.getColumn())
            # check down
            elif self.pitch.isPlayerOnPosition(snitch.getRow()+1, snitch.getColumn()):
                # run away, up
                if self.newPosition(snitch, snitch.getRow()-1, snitch.getColumn()):
                    self.pitch.clearPosition(
                        snitch.getRow()+1, snitch.getColumn())
            else:
                # move random if no player next to
                randomNumber = random.randint(0, 3)
                if randomNumber == 0:  # left
                    if self.newPosition(snitch, snitch.getRow(), snitch.getColumn()-1):
                        self.pitch.clearPosition(
                            snitch.getRow(), snitch.getColumn()+1)
                elif randomNumber == 1:  # right
                    if self.newPosition(snitch, snitch.getRow(), snitch.getColumn()+1):
                        self.pitch.clearPosition(
                            snitch.getRow(), snitch.getColumn()-1)
                elif randomNumber == 2:  # up
                    if self.newPosition(snitch, snitch.getRow()-1, snitch.getColumn()):
                        self.pitch.clearPosition(
                            snitch.getRow()+1, snitch.getColumn())
                elif randomNumber == 3:  # down
                    if self.newPosition(snitch, snitch.getRow()+1, snitch.getColumn()):
                        self.pitch.clearPosition(
                            snitch.getRow()-1, snitch.getColumn())

    def update(self):
        self.checkSnitch()
        self.updatePitchSeekers()
        self.moveSnitch()
        self.updatePitchSnitch()

    def checkSnitch(self):
        snitch = self.goldenSnitch
        seeker1 = self.teams[0].seeker
        seeker2 = self.teams[1].seeker

        if snitch.getRow() == seeker1.getRow() and snitch.getColumn() == seeker1.getColumn():
            self.awardPoints(self.teams[0])
            snitch.captured()
        elif snitch.getRow() == seeker2.getRow() and snitch.getColumn() == seeker2.getColumn():
            self.awardPoints(self.teams[1])
            snitch.captured()

    def updatePitchSeekers(self):
        self.pitch.placeOnPitch(
            self.charDict["seeker"], self.teams[0].seeker.getRow(), self.teams[0].seeker.getColumn())
        self.pitch.placeOnPitch(
            self.charDict["seeker"], self.teams[1].seeker.getRow(), self.teams[1].seeker.getColumn())

    def updatePitchSnitch(self):
        if self.goldenSnitch.isFree():
            self.pitch.placeOnPitch(
                self.charDict["goldenSnitch"], self.goldenSnitch.getRow(), self.goldenSnitch.getColumn())

    def draw(self):
        return str(self.pitch)

    def printPoints(self):
        printMe = "Points: Team " + self.teams[0].getName() + \
            " " + str(self.teams[0].getPoints())
        printMe += " : " + \
            str(self.teams[1].getPoints()) + " Team " + self.teams[1].getName()
        return printMe

    def printMoves(self):
        printMe = "Moves: Team " + self.teams[0].getName() + \
            " " + str(self.teams[0].seeker.getMovesMade())
        printMe += " : " + \
            str(self.teams[1].seeker.getMovesMade()) + \
            " Team " + self.teams[1].getName()
        return printMe

    def printLevel(self):
        return "Level " + str(self.level + 1)

    def newPosition(self, object, newRow, newColumn):
        if self.pitch.isPositionFree(newRow, newColumn):
            object.move(newRow, newColumn)
            return True
        else:
            return False

    def recognizeInput(self, char):
        char = char.upper()
        if char == "A":
            # seeker1 left
            seeker = self.teams[0].seeker
            if self.newPosition(seeker, seeker.getRow(), seeker.getColumn()-1):
                self.pitch.clearPosition(seeker.getRow(), seeker.getColumn()+1)
                seeker.addMovesMade()
        elif char == "D":
            # seeker1 right
            seeker = self.teams[0].seeker
            if self.newPosition(seeker, seeker.getRow(), seeker.getColumn()+1):
                self.pitch.clearPosition(seeker.getRow(), seeker.getColumn()-1)
                seeker.addMovesMade()
        elif char == "W":
            # seeker1 up
            seeker = self.teams[0].seeker
            if self.newPosition(seeker, seeker.getRow()-1, seeker.getColumn()):
                self.pitch.clearPosition(seeker.getRow()+1, seeker.getColumn())
                seeker.addMovesMade()
        elif char == "S":
            # seeker1 down
            seeker = self.teams[0].seeker
            if self.newPosition(seeker, seeker.getRow()+1, seeker.getColumn()):
                self.pitch.clearPosition(seeker.getRow()-1, seeker.getColumn())
                seeker.addMovesMade()
        elif char == "J":
            # seeker2 left
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow(), seeker.getColumn()-1):
                self.pitch.clearPosition(seeker.getRow(), seeker.getColumn()+1)
                seeker.addMovesMade()
        elif char == "L":
            # seeker2 right
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow(), seeker.getColumn()+1):
                self.pitch.clearPosition(seeker.getRow(), seeker.getColumn()-1)
                seeker.addMovesMade()
        elif char == "I":
            # seeker2 up
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow()-1, seeker.getColumn()):
                self.pitch.clearPosition(seeker.getRow()+1, seeker.getColumn())
                seeker.addMovesMade()
        elif char == "K":
            # seeker2 down
            seeker = self.teams[1].seeker
            if self.newPosition(seeker, seeker.getRow()+1, seeker.getColumn()):
                self.pitch.clearPosition(seeker.getRow()-1, seeker.getColumn())
                seeker.addMovesMade()
        else:
            print("input fail")
