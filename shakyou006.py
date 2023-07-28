# 第5章
# イテラブル＝繰り返し可能
# ミュータブル＝変更可能

fruit = ["Apple", "Orange", "Pear"]
print(fruit[0])
print(fruit[1])
print(fruit[2])

colors = ["blue", "green", "yellow"]
print(colors)
colors[2] = "red"
print(colors)

item = colors.pop()  # popメソッド　リストの最後尾を取り出す
print(item)
print(colors)

colors1=["blue","green","yellow"]
colors2=["orange","pink","black"]
colors3=colors1+colors2
print(colors3)

