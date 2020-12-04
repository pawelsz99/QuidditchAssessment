# -------------------------------------------------------------------------------
# Name:        GoldenSnitch.py
# Purpose:
#
# Author:      Pawel Sznura
#
# Created:     03/12/2020
# Copyright:   (c) Pawel Sznura 2020
# -------------------------------------------------------------------------------

from MovingObject import MovingObject


class GoldenSnitch(MovingObject):
    def __init__(self, row, column):
        super().__init__(row, column)
        self.free = True

    def isFree(self):
        return self.free
