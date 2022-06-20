import random
print('Добро пожаловать в числовую угадайку')
print("Укажите максимальное число для угадывания:")

def is_valid(num):
    if num.isdigit():
        if 1 <= int(num) <= int(max_n)+1:
            return True
        else:
            return False
    else:
        return False

max_n = input()

while True:
    if is_valid(max_n):
        break
    else:
        print("Укажите целое цифровое значение:")
        max_n = input()

rand_numb = random.randint(1, int(max_n))
counter = 0

print("Какое число загадано:")

while True:
    inp = input()
    if is_valid(inp): 
        inp = int(inp)
        if inp < rand_numb:
            counter +=1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif inp > rand_numb:
            counter +=1
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали c {counter} попытки, поздравляем!')
            print("Хотите сыграть снова?(yes/no)")
            cont = input()
            if cont == "yes":
                print("Какое число загадано:")
                counter = 0
                rand_numb = random.randint(1, int(max_n))
                continue
            else:
                break
    else:
        print(f'А может быть все-таки введем целое число от 1 до {max_n}?')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
