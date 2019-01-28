# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def n_gram(target, n) -> list:
    """creates n_gram

    Parameters
    ----------
    target : str or list of str
        sentenst or list of words
    n : int

    Returns
    -------
    list
        the list stors chars or words divided into n_gram
    """
    result = []

    for i in range(0, len(target) - n + 1):
        result.append(target[i:i + n])

    return result

word1 = 'paraparaparadise'
word2 = 'paragraph'

set_a = set(n_gram(word1, 2))
set_b = set(n_gram(word2, 2))

set_union = set_a | set_b
set_intersection = set_a & set_b
set_difference = set_a - set_b

print(
    'union {} \n' +
    'intersection {}\n'+
    'difference {}'.
    format(set_union, set_intersection, set_difference)
)