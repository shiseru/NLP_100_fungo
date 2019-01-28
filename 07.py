# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

def output_phrase(x: int, y: str, z: str):
    return str(x) + '時の' + y + 'は' + z

print(output_phrase(12, "気温", str(22.4)))
