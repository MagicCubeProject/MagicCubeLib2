from unittest import TestCase

from Enumerations.facet import Facet
from MagicCube.MagicCube import MagicCube


class TestMagicCell(TestCase):
    def test_distance(self):
        mc=MagicCube()
        d = mc.positionaldistances()
        print(d)
        mc.rotate(Facet.UP)
        d = mc.positionaldistances()
        print(d)
        print(10*'-_')
        mc.rotate(Facet.FRONT)
        print(str(mc))
        d = mc.positionaldistances()
        print(d)
        # mc.rotate(Facet.LEFT)
        # d = mc.positionaldistances()
        # print(d)
        pass
