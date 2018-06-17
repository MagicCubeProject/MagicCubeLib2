from enum import Enum, auto


class Facet(Enum):
    FRONT   = 0
    RIGHT   = 1
    DOWN    = 2
    UP      = 3
    LEFT    = 4
    BACK    = 5

    def isParalell(self,compareFacet):
        if self.value+compareFacet.value is 5:
            return True
        else:
            return False

    def __str__(self):
        return self.name[0]

    def neighbors(self):
        if self is Facet.FRONT:
            return [Facet.UP,Facet.RIGHT,Facet.DOWN,Facet.LEFT]
        elif self is Facet.RIGHT:
            return [Facet.BACK,Facet.DOWN,Facet.FRONT,Facet.UP]
        elif self is Facet.DOWN:
            return [Facet.RIGHT,Facet.BACK,Facet.LEFT,Facet.FRONT]
        elif self is Facet.UP:
            return [Facet.LEFT,Facet.BACK,Facet.RIGHT,Facet.FRONT]
        elif self is Facet.LEFT:
            return [Facet.FRONT,Facet.DOWN,Facet.BACK,Facet.UP]
        elif self is Facet.BACK:
            return [Facet.DOWN,Facet.RIGHT,Facet.UP,Facet.LEFT]
        else:
            return None
