""" exercice 2 """

__author__ = "sossou_e"


def filter_even_numbers(numbers: list[int]) -> list:
    """ retourner les nombres pares d'une liste """
    return [x for x in numbers if x % 2 == 0]
