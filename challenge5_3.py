# 辞書を作る

codes = {"1": "Name",
         "2": "Height",
         "3": "Weight",
         "4": "BDay"}

my_data = {"Name": "Kazuhisa Yamashita",
           "Height": "178cm",
           "Weight": "81Kg",
           "BDay": "5.15.19XX"
           }

print(codes)
# print(my_data)
in_code = input("Enter the number of the information you want to see:")
print(codes[in_code], ":", my_data[codes[in_code]])
