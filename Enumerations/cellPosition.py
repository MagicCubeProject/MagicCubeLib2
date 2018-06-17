from enum import Enum


class CellPosition(Enum):
    CENTER      = 0
    NORTH       = 1
    NORTH_EAST  = 2
    EAST        = 3
    SOUTH_EAST  = 4
    SOUTH       = 5
    SOUTH_WEST  = 6
    WEST        = 7
    NORTH_WEST  = 8

    def isEdge(self):
        if(self.value%2==1):
            return True
        else:
            return False

    def isCorner(self):
        if(self.value%2==0 and self.value!=0):
            return True
        else:
            return False

    def left(self):
        return CellPosition(self.value-1) if  self is not CellPosition.NORTH else CellPosition.NORTH_WEST

    def right(self):
        return  CellPosition(self.value+1) if  self is not CellPosition.NORTH_WEST else CellPosition.NORTH
