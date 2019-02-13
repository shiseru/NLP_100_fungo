# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

f = 'hightemp.txt'
with open(f) as data_file:
    for line in data_file:
        print(line.replace('\t', ' '), end='')

# unix command
# sed 's/\t/ /g' hightemp.txt