import unittest

from anagramas.anagramas import gerador_de_anagrama


class AnagramaTest(unittest.TestCase):
    def test_anagramas_biro(self):
        anagramas = gerador_de_anagrama('biro')
        expected = ['biro', 'bior', 'brio', 'broi', 'boir', 'bori',
                    'ibro', 'ibor', 'irbo', 'irob', 'iobr', 'iorb',
                    'rbio', 'rboi', 'ribo', 'riob', 'roib', 'robi',
                    'obir', 'obri', 'oibr', 'oirb', 'orbi', 'orib']
        for word in expected:
            with self.subTest():
                self.assertIn(word, anagramas)

    def test_anagramas_abc(self):
        anagramas = gerador_de_anagrama('abc')
        expected = ['abc', 'bca', 'cab',
                    'bac', 'acb', 'cba']
        for word in expected:
            with self.subTest():
                self.assertIn(word, anagramas)
