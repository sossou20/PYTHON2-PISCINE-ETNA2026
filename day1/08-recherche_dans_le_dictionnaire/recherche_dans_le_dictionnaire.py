""" exercice 08 """

__author__ = "sossou_e"


def get_value_from_dict(d: dict, key: int) -> str:
    """ presence de cle dans une dictionnaire """
    if key in d:
        return d[key]
    return "cle non trouve"
