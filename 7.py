num = int(input())
last_n = num % 10

# обрабатываем все ситуации, учитывая исключения (числа от 11 до 19)

if last_n == 1 and num != 11:
    print(num, 'korova')

elif ((last_n == 2 or last_n == 3 or last_n == 4)
      and (num > 21 or num < 5)):
    print(num, 'korovy')

else:
    print(num, 'korov')
