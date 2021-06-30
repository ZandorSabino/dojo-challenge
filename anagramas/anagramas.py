"""
Escreva um programa que gere todos os anagramas potenciais de uma string.

Por exmplo, os anagramas potenciais de "biro" são:

biro bior brio broi boir bori
ibro ibor irbo irob iobr iorb
rbio rboi ribo riob roib robi
obir obri oibr oirb orbi orib

Traduzido de: http://www.cyber-dojo.com
"""
from itertools import permutations


def gerador_de_anagrama(word):
    anagramas = []
    for x in permutations(word):
        anagramas.append(''.join(x))
    return anagramas
