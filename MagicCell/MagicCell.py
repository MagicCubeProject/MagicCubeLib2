from Enumerations.cellPosition import CellPosition
from Enumerations.facet import Facet


class MagicCell(object):
    """
    This class Describe Cell of Rubic's Cube : Values and operations on it
    """
    def __init__(self, value: Facet, position: CellPosition , facet: Facet):
        self.value: Facet = value
        self.position: CellPosition = position
        self.facet: Facet = facet

    def __str__(self):
            return str(self.value.value)

    def isPosition(self,position: CellPosition):
        return position == self.position

    def moveTo(self,position: CellPosition,facet: Facet):
        self.position = position
        self.facet = facet

    def distance(self):
        x_distance:int = 0
        y_distance:int = 0
        if self.value is self.facet:
            if self.position is CellPosition.CENTER:
                pass
            elif self.position.isEdge():
                x_distance+=1
            elif self.position.isCorner():
                x_distance+=1
                y_distance+=1
        elif self.value.isParalell(self.facet):
            x_distance+=5
            if self.position.isCorner():
                y_distance+=1
        else:
            if self.position.isEdge():
                neighborInex = int((self.position.value-1)/2)
                neighbor = self.facet.neighbors()[neighborInex]
                if neighbor is self.value:
                    x_distance+=2
                elif self.value.isParalell(neighbor):
                    x_distance+=4
                else:
                    x_distance+=3
                    y_distance+=1
            elif self.position.isCorner():
                leftNeighborInex = int((self.position.left.value-1)/2)
                leftNeighbor = self.facet.neighbors()[leftNeighborInex]

                rightNeighborInex = int((self.position.right.value-1)/2)
                rightNeighbor = self.facet.neighbors()[rightNeighborInex]
                if leftNeighbor is self.value or rightNeighbor is self.value:
                    x_distance+=2
                    y_distance+=1
                else:
                    x_distance+=4
                    y_distance+=1
        distance_value:int=x_distance**2+y_distance**2
        return distance_value
    # def distance(self):
    #     x_part:int = 0
    #     y_part:int = 0
    #     parallel_x_part:int = 0
    #     parallel_y_part:int = 0
    #
    #     if self.position is CellPosition.CENTER:
    #         parallel_x_part+=6
    #     elif self.position.isCorner():
    #         if self.value is self.facet:
    #             x_part+=1
    #             y_part+=1
    #             parallel_x_part+=5
    #             parallel_y_part+=1
    #         elif self.value.isParalell(self.facet):
    #             x_part+=5
    #             y_part+=1
    #             parallel_x_part+=1
    #             parallel_y_part+=1
    #         else:
    #             x_part+=4
    #             y_part+=1
    #             parallel_x_part+=2
    #             parallel_y_part+=1
    #     elif self.position.isEdge():
    #         if self.value is self.facet:
    #             x_part+=1
    #             parallel_x_part+=5
    #         elif self.value.isParalell(self.facet):
    #             x_part+=5
    #             parallel_x_part+=1
    #         else:
    #             x_part+=3
    #             y_part+=1
    #             parallel_x_part+=3
    #             parallel_y_part+=1
    #
    #     distance_value:int = x_part**2+y_part**2+parallel_x_part**2+parallel_y_part**2
    #     return distance_value


