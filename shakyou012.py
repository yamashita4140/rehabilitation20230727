# リストの中にタプル
locations = []  # <- 空のリストを作成

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

# タプルの中にリスト
eights = ["Edgar Allan Poe", "Charles Dickens"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]

authors = (eights, nines)

print(authors)

# リストの中に辞書

bday = {"Hemingway": "7.21.1899",
        "Fitzgerald": "9.24.1896"}
my_list = [bday]
print(my_list)
print(my_list[0]["Hemingway"])
print(type(my_list))
print(type(my_list[0]))

# タプルの中に辞書
my_tuple = (bday,)
print(my_tuple)
print(type(my_tuple))
