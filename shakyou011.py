# コンテナの中のコンテナ

# listの中にlistを格納する

lists = []  # <- 空のリストを作成

rap = ["カニエ・ウェスト", "ジェイ・Z", "エムネム", "ナズ"]
rock = ["ボブ・ディラン", "ザ・ビートルズ", "レッド・ツェッペリン"]
djs = ["ゼッズ・デッド", "ティエスト"]

lists.append(rap)  # <- 空のリスト「lists」にリスト「rap」を追加
lists.append(rock)  # <- 空のリスト「lists」にリスト「rock」を追加
lists.append(djs)  # <- 空のリスト「lists」にリスト「djs」を追加

print(lists)

rap.append("ケンドリック・ラマー")  # <- rapに要素を追加
print(rap)
print(lists)  # <- 「rap」への要素追加が「lists」にも反映されている!!
