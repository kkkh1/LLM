import re

global matches

with open('./gptres.text','r') as f:
    text=f.read()

# 正規表現を使って「？」で囲まれた文字列を抽出するパターンを定義
    pattern = r'\?(.*?)\?'

# テキストからパターンにマッチする部分を抽出し、リストに格納
    matches = re.findall(pattern, text)
    

# 結果を出力
    print(matches)
    print(matches[0])
