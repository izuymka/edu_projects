import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
symbols = '!#$%&*+-=?@^_'
chars = ''

number_password = int(input('Укажите количество генерируемых паролей: '))
len_password = int(input('Укажите длину одного пароля: '))
dig_on = input('Включать ли цифры 0123456789 в пароль? (y/n) ')
upp_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
low_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
sym_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')

if dig_on == 'y':
    chars += digits
if upp_on == 'y':
    chars += uppercase_letters
if low_on == 'y':
    chars += lowercase_letters
if sym_on == 'y':
    chars += symbols
if excOn == 'y':
    for c in 'il1Lo0O':
        chars.replace(c,'')

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

for _ in range(number_password):
    print(generate_password(len_password, chars))

