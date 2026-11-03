"""exercice 6"""

__author__ = "sossou_e"


def extract_valid_pairs(pairs: list) -> list:
    """ une liste ne contenant pas le paire de l'autre """
    return [p for p in pairs if isinstance(p[0], int)]
