text = input("Введите текст для шифровки:")
language = input("На каком языке текст(eng/ру):")
direction = input("Шифрование или дешифрование(ш/д):")
print("Укажите шаг сдвига:")
step = int(input())

alph_eng_low = "abcdefghigklmnopqrstuvwxyz"
alph_eng_high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alph_rus_low = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alph_rus_high = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЭЮЯ"


def encrypt(inp, alph_low, alph_high):
    elem = 0
    outp = []
    for simb in range(len(inp)):
        if inp[simb] in alph_low:
            elem = alph_low.index(inp[simb])
            if elem + step > len(alph_low):
                outp.append(alph_low[elem + step - len(alph_low)])
            else:
                outp.append(alph_low[elem + step])
        elif inp[simb] in alph_high:
            elem = alph_high.index(inp[simb])
            if elem + step > len(alph_high):
                outp.append(alph_high[elem + step - len(alph_high)])
            else:
                outp.append(alph_high[elem + step])
        else:
            outp.append(inp[simb])
    return outp


def decipher(inp, alph_low, alph_high):
    elem = 0
    outp = []
    for simb in range(len(inp)):
        if inp[simb] in alph_low:
            elem = alph_low.index(inp[simb])
            if elem - step < 0:
                outp.append(alph_low[elem - step + len(alph_low)])
            else:
                outp.append(alph_low[elem - step])
        elif inp[simb] in alph_high:
            elem = alph_high.index(inp[simb])
            if elem - step < 0:
                outp.append(alph_high[elem - step + len(alph_high)])
            else:
                outp.append(alph_high[elem - step])
        else:
            outp.append(inp[simb])
    return outp


if direction == "ш":
    if language == "eng":
        print(*encrypt(text, alph_eng_low, alph_eng_high), sep='')
    elif language == "ру":
        print(*encrypt(text, alph_rus_low, alph_rus_high), sep='')
elif direction == "д":
    if language == "eng":
        print(*decipher(text, alph_eng_low, alph_eng_high), sep='')
    elif language == "ру":
        print(*decipher(text, alph_rus_low, alph_rus_high), sep='')