import unittest

from Creature.Creature import Creature
from Creature.Genetics.SimpleRandomGene import SimpleRandomGene
from TestUtil.TestCaseExtension import TestCaseExtension


class CreatureTest(TestCaseExtension):
    def test_creature(self):
        test_creature = Creature(SimpleRandomGene(10))
        self.assertEqual(test_creature.geneticMakeup, SimpleRandomGene(10))


if __name__ == '__main__':
    unittest.main()
