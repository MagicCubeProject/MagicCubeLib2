from Enumerations.cellPosition import CellPosition
from Enumerations.facet import Facet
from MagicFacet.MagicFacet import MagicFacet


class MagicCube(object):
    def __init__(self,numeric:str=None):
        self.magicFacets = list()
        if numeric is None:
            for facet in Facet:
                self.magicFacets.append(
                    MagicFacet(facet)
                )
        else:
            for i in range(6):
                self.magicFacets.append(
                    MagicFacet(None,numeric[i*9:(i+1)*9])
                )

    def __getitem__(self,facet:Facet):
        for magicFacet in self.magicFacets:
            if magicFacet.isFacet(facet):
                return magicFacet

    def __str__(self):
        result = str()
        for facet in Facet:
            result+=str(self[facet])
        return result


    def rotateLie(self,facet:Facet,reverse = False):
        tempLines = list()
        neighbors = self[facet].value.neighbors()
        for neighbor in neighbors:
            print(neighbor)
            secondaryNeighbors = neighbor.neighbors()
            for secondaryNeighborIndex in range(4):
                secondaryNeighbor = secondaryNeighbors[secondaryNeighborIndex]
                if secondaryNeighbor is facet:
                    cellPosition = CellPosition(secondaryNeighborIndex*2+1)
                    neighborFacet = self[neighbor]
                    tempLine = neighborFacet.getLine(cellPosition)
                    tempLines.append(tempLine)
        for neighborIndex in range(4):
            neighbor = neighbors[neighborIndex]
            if(reverse):
                tempLine = tempLines[(neighborIndex-1)%4]
            else:
                tempLine = tempLines[(neighborIndex+1)%4]
            for posIndex in range(4):
                if self[neighbor][CellPosition(posIndex*2+1)] is None:
                    pos = CellPosition(posIndex*2+1)
                    continue
            self[neighbor].setLine(tempLine,pos)

    def rotate(self,facet:Facet,reverse = False):
        self[facet].rotate(reverse)
        self.rotateLie(facet,reverse)

    def positionaldistances(self):
        distancesList =list()
        for facet in Facet:
            tempDistances = self[facet].distances()
            soertedDistances = sorted(tempDistances)
            distancesList.append(soertedDistances)
        return distancesList

    def distances(self):
        distancesList = self.positionaldistances()
        sortedDistancesList = sorted(distancesList)
        return sortedDistancesList
