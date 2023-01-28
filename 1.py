'''n = int(input('Введите n: '))
m = int(input('Введите m: '))

d = (m + n - 1) // n

print(d)'''

n = int(input('Скорость в день: '))
m = int(input('Расстояние км: '))

'''t = m//n
ostatok = (m % n) > 0
ostatokBool = bool(ostatok)
ostatokDays = int(ostatok)'''


print('Дней ', (m+n-m%n)//n)