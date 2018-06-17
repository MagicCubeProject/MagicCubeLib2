from unittest import TestCase

from Enumerations.cellPosition import CellPosition
from Enumerations.facet import Facet
from MagicCube.MagicCube import MagicCube


class TestMagicCube(TestCase):
    def test_init(self):
        mc = MagicCube()
        for facet in Facet:
            self.assertEqual(str(mc[facet]),str(facet.value)*9)
        print(str(mc))

        stringValue = "000000000111111111222222222333333333444444444555555555"
        mc2 = MagicCube(stringValue)
        for facet in Facet:
            self.assertEqual(str(mc2[facet]),str(facet.value)*9)

    def test_rotateLine(self):
        mc = MagicCube()
        d = mc.distances()
        mc.rotateLie(Facet.FRONT)
        mc.rotateLie(Facet.FRONT,True)

        mc.rotate(Facet.FRONT)
        pass
