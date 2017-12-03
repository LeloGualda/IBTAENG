from unittest import TestCase
from Combinacoes import  Combinacoes

class TestCombine(TestCase):
    def test_referencialN1(self):
        vetor = ["A"]
        self.assertEqual(Combinacoes.combinar(vetor),[('A',)])
    def test_referencialN2(self):
        vetor = ["A","B"]
        self.assertEqual(Combinacoes.combinar(vetor),[('A',),('B',),('A','B')])

    def test_referencialN3(self):
        vetor = ["A","B","C"]
        self.assertEqual(Combinacoes.combinar(vetor),[('A',),('B',),('C',),('A','B'),('A','C'),('B','C'),('A','B','C')])
