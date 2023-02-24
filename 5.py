a, b = int(input()), int(input())

# проверяем все возможные исходы, учитывая в начале что a != 0

if a == 0 and b != 0:
    print('NO')

elif a * (-b // a) + b != 0:
    print('NO')

elif a == 0 and b == 0:
    print('INF')

else:
    print(-b // a)