# 辞書
# 辞書はミュータブルなコンテナ
# リスト、タプルとの違いは、キーとバリューのペアで管理される
# 「キー」はイミュータブルでなければならない
# 「バリュー」はミュータブルで良い

# 辞書の作成
fruit = {"Apple": "Red",
         "Banana": "Yellow"}
print(fruit)

# 辞書を作成後、キーバリューペアを追加
facts = dict()  # <- 空の辞書を作成

facts["code"] = "fun"  # <- 新しいキーバリューペアを追加
print(facts["code"])
facts["Bill"] = "Gates"
print(facts["Bill"])
facts["founded"] = 1776
print(facts["founded"])

# 「in演算子」は「キー」が含まれているかを確認することはできるが
# 「バリュー」に含まれているかを確認することはできない
bill = {"Bill Gates": "charitable"}
print("Bill Gates" in bill)

# 辞書からキーバリューペアを削除　delを使用する
books={"Dracula":"Stoker",
       "1984":"Orwell",
       "The Trial":"Kafka"}
print(books)
del books["The Trial"]
print(books)
