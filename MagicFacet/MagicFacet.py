from Enumerations.cellPosition import CellPosition
from Enumerations.facet import Facet
from MagicCell.MagicCell import MagicCell


class MagicFacet(object):
    def __init__(self,facet:Facet,numeric:str = None):
        self.value = facet
        self.cells:list = list()
        if numeric is None:
            for position in CellPosition:
                self.cells.append(MagicCell(facet,position,facet))
        else:
            self.value: Facet = Facet(int(numeric[0]))
            for i in range(len(numeric)):
                position = CellPosition(i)
                value = Facet(int(numeric[i]))
                self.cells.append(MagicCell(value,position,self.value))

    def __getitem__(self,position:CellPosition):
        for cell in self.cells:
            if cell.isPosition(position):
                return cell

    def __str__(self):
        string:str = ""
        for position in CellPosition:
            string += str(self[position])
        return string

    def isFacet(self,facet:Facet):
        return self.value==facet

    def rotate(self,reverse = False):
        for cell in self.cells:
            if cell.position is not CellPosition.CENTER:
                if reverse:
                    if cell.position is CellPosition.NORTH_EAST:
                        nextPosition = CellPosition(8)
                    else:
                        nextPosition = CellPosition((cell.position.value+6)%8)
                else:
                    if cell.position is CellPosition.SOUTH_WEST:
                        nextPosition = CellPosition(8)
                    else:
                        nextPosition = CellPosition((cell.position.value+2)%8)
                cell.moveTo(nextPosition,self.value)

    def getLine(self,cellPosition:CellPosition):
        tempList:list=list()
        tempList.append(self[cellPosition.left()])
        tempList.append(self[cellPosition])
        tempList.append(self[cellPosition.right()])
        self.cells.remove(self[cellPosition.left()])
        self.cells.remove(self[cellPosition])
        self.cells.remove(self[cellPosition.right()])
        return tempList

    def setLine(self,cells:list,cellPosition:CellPosition):
        cells[0].moveTo(cellPosition.left(),self.value)
        cells[1].moveTo(cellPosition,self.value)
        cells[2].moveTo(cellPosition.right(),self.value)
        self.cells.extend(cells)

    def distances(self):
        distances = list()
        for cell in self.cells:
            distances.append(cell.distance())
        return distances

