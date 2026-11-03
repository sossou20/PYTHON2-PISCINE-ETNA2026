""" exercice 4"""

__author__ = "sossou_e"


def replace_multiples_of_3(numbers: list) -> list:
    """ retourne une multiple de 3"""
    return ["Fizz" if x % 3 == 0 else x for x in numbers]
