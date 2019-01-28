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

target = 'I am an NLper'
words_target = target.split()

word_n_gram = n_gram(words_target, 2)
print(word_n_gram)

char_n_gram = n_gram(target, 2)
print(char_n_gram)
