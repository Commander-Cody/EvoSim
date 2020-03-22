import unittest

from Creature.Genetics.SimpleRandomGene import SimpleRandomGene


class SimpleRandomGeneTest(unittest.TestCase):
    def test_create_copy(self):
        gene = SimpleRandomGene(100)
        self.assertEqual(gene.value, 100)

    def test_genes_are_random(self):
        gene1 = SimpleRandomGene()
        gene2 = SimpleRandomGene()

        self.assertEqual(type(gene1.value), int)
        self.assertEqual(type(gene2.value), int)
        self.assertNotEqual(gene1.value, gene2.value)

    def test_replication_can_cause_mutation(self):
        SimpleRandomGene.default_mutation_chance = 1
        gene1 = SimpleRandomGene()
        gene2 = gene1.replicate()

        self.assertNotEqual(gene1.value, gene2.value)

    def test_mutations_differ_by_power_of_two(self):
        SimpleRandomGene.mutation_chance = 1
        gene1 = SimpleRandomGene()
        gene2 = gene1.replicate()
        diff = abs(gene1.value - gene2.value)

        self.assertTrue(((diff & (diff - 1)) == 0))

    def test_replication_can_be_perfect(self):
        SimpleRandomGene.mutation_chance = 0
        gene1 = SimpleRandomGene()
        gene2 = gene1.replicate()

        self.assertEqual(gene1.value, gene2.value)

    def test_equality(self):
        gene1 = SimpleRandomGene(1)
        gene2 = SimpleRandomGene(3)
        gene3 = SimpleRandomGene(3)

        self.assertTrue(gene1 == gene1)
        self.assertTrue(gene1 != gene2)
        self.assertTrue(gene2 == gene3)
        self.assertTrue(gene1 != 1)


if __name__ == '__main__':
    unittest.main()
