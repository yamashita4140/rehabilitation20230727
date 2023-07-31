# タプル
# リストと異なり「イミュータブル（変更不可）」
# 変更・追加・削除　不可

# タプルにオブジェクトを追加
rndm = ("M.Jackson", 1958, True)
print(rndm)

# タプルの要素が一つだけの場合、必ず末尾にカンマを置くこと
my_tuple = ("self_taught",)
print(my_tuple)

# タプルから要素を取り出すときは、リストと同じ
dys = ("1984", "Brave New World", "Fahrenheit 451")
print(dys[2])

# リストと同じように「in演算子」を使うこともできる
print("1984" in dys)
