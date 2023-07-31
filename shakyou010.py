# 辞書を使ったプログラム
# 辞書を作成し、”数字”を入力させる。入力した”数字”がキーに含まれていれば、該当するバリューを出力する

songs={"1":"fun",
       "2":"blue",
       "3":"me",
       "4":"floor",
       "5":"live"}

n=input("数字を入力してください：")
if n in songs:
    song=songs[n]
    print(song)
else:
    print("ねぇよ")

