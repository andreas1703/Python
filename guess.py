import random
guessnumber = random.randint(0,10)
print ('Введите число от 0 до 10')
m = int(input())
while m != guessnumber:
    if m < guessnumber:
        print ('Ваше число слишком маленькое', 'Поробуйте снова')
        m = input()
        m = int(m)
    if m > guessnumber:
        print ('Ваше число слишком большое', 'Попробуйте снова')
        m = input()
        m = int(m)
if m == guessnumber:
    print('ПОЗДРАВЛЯЮ ВЫ УГАДАЛИ')