# 4章チャレンジ4

def func_a(num1):
    return num1 // 2


def func_b(num2):
    return num2 * 4


num_input = int(input("input num:"))
result_a = func_a(num_input)
result_b = func_b(result_a)
print("result_a =", result_a)
print("result_b =", result_b)
