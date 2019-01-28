"""
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
（例えば
"I couldn't believe that I could actually understand what I was reading :
the phenomenal power of the human mind ."
）
を与え，その実行結果を確認せよ．
"""
import random


def typoglycemia(text: str):
    """if length of word is grater then 4, shufflethe word except the first
    and last char

    Parameters
    ----------
    text : str

    Returns
    -------
    str
        shuffled text
    """
    words_list = text.split()

    shuffled_text = []

    for word in words_list:
        if len(word) <= 4:
            pass
        else:
            chr_list = list(word[1:-1])
            random.shuffle(chr_list)
            word = word[0] + ''.join(chr_list) + word[-1]

        shuffled_text.append(word)
    return ' '.join(shuffled_text)

text = """
       I couldn't believe that I could actually understand what I was reading :
       the phenomenal power of the human mind .
       """

print(typoglycemia(text))
