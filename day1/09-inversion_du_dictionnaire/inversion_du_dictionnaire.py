""" exercic 9 """

__author__ = "sossou_e"


def invert_dict(d: dict) -> dict:
    """ inverser les cles et les valeur dun dictionnaire """
    inverted = {}
    for k, v in d.items():
        inverted[v] = k
    return inverted
