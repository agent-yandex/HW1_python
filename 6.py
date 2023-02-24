a, b, c = int(input()), int(input()), int(input())

# считаем дискриминант и по его значению определяем ответ
d = b**2 - 4 * a * c

if d > 0:
    print((-b + d**0.5) / 2 * a, (-b - d**0.5) / 2 * a)
elif d == 0:
    print((-b + d**0.5) / 2 * a)