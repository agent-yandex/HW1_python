x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

# если точки находятся в одной плоскости, то при перемножении
# они в любом случае будут больше или равны нулю

if x1 * x2 > 0 and y1 * y2 > 0:
    print('YES')
else:
    print('NO')