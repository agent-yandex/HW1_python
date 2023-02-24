n = int(input())

# считаем "идеальный" вариант совпадения
count_60 = n // 60
n = n % 60
count_10 = n // 10
count_1 = n % 10

# переход к более выгодному варианту (из единиц в десятки, из десяток в 60)
if count_1 == 9:
    count_10 += 1
    count_1 = 0
if count_10 > 3:
    count_60 += 1
    count_10 = 0

print(count_1, count_10, count_60)
