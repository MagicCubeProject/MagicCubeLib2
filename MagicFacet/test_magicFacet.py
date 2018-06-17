from unittest import TestCase

from Enumerations.cellPosition import CellPosition
from Enumerations.facet import Facet
from MagicFacet.MagicFacet import MagicFacet


class TestMagicFacet(TestCase):
    def test_init(self):
        mf = MagicFacet(Facet.FRONT)
        strvalue = "123405321"
        mf2 = MagicFacet(Facet.FRONT,strvalue)
        self.assertEqual(str(mf2),strvalue)

    def test_rotate(self):
        strvalue = "123405321"
        mf2 = MagicFacet(Facet.FRONT,strvalue)
        self.assertEqual(str(mf2),strvalue)
        mf2.rotate()
        self.assertEqual(str(mf2),"121234053")
        mf2.rotate(True)
        self.assertEqual(str(mf2),strvalue)
        temp_cells = mf2.getLine(CellPosition.NORTH)
        self.assertEqual(str(mf2),"1NoneNone40532None")
        for cell in temp_cells:
            cell.value = Facet.FRONT
            cell.facet = Facet.UP
        mf2.setLine(temp_cells,CellPosition.NORTH)
        self.assertEqual(str(mf2),"100405320")

    def test_neighbors(self):
        a = Facet.LEFT.neighbors()
        print(a)


    def test_distance(self):
        mf = MagicFacet(Facet.FRONT)
        d = mf.distances()
        print(d)
        strvalue = "123405321"
        mf2 = MagicFacet(Facet.FRONT,strvalue)
        d2 = mf2.distances()
        print(d2)

