x = int(input())

# разделим римское число на 3 части
# 1 часть - кол-во L
# 2 часть - кол-во X
# 3 часть - разряд едениц
p_1, p_2, p_3 = '', '', ''
count = 0

# прорабатываем все исключения и заполняем все части

if x >= 50 and x < 90:
    p_1 = 'L'
    count += 1

if x - 50 * count >= 10 and x != 40:
    p_2 = 'X' * ((x - 50 * count) // 10)

if x % 10 > 4 and x % 10 != 9:
    p_3 = 'V' + 'I' * (x % 10 - 5)

elif x % 10 < 4:
    p_3 = 'I' * (x % 10)

elif x % 10 == 4:
    p_3 = 'IV'

else:
    p_3 = 'IX'

if x == 100:
    print('C')

elif x >= 90:
    p_1 = 'XC'
    print(p_1 + p_3)

elif x >= 40 and x < 50:
    p_1 = 'XL'
    print(p_1 + p_3)

else:
    print(p_1 + p_2 + p_3)
