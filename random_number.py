def number_control(num):
    while True:
        if not num.isdigit():
            num = input('Введите ЦИФРУ')
        elif num.isdigit():
            break
    return num

print('\n''Привет, это игра "Угадайка чисел". ')
print('\n''Программа уже сгенерировала число от 1 до 100.')
print('Твоя задача его угадать.')
print('Будут подсказки и 6 попыток. \nУдачи! :)')

while True:
    count = 0
    import random
    import time
    import os

    random_number = random.randint(0, 100)
    user_number = input('Введите число от 0 до 100. ')
    user_number = number_control(user_number)
    user_number = int(user_number)
    count += 1

    while True:
        if user_number > random_number:
            count += 1
            if count == 4 or count == 5:
                print('\n'f'У Вас осталось', 7 - count, 'попытки.''\n')
            elif count == 6:
                print('\n'f'У Вас осталось', 7 - count, 'попытка.''\n')
            elif count == 7:
                print('Вы исчерпали 6 попыток. Игра окончена.')
                print('Число которое было загадано:', random_number)
                break
            print('Вы ввели число больше! попробуйте ещё раз.')
            user_number = input('Введите число: ')
            user_number = number_control(user_number)
            user_number = int(user_number)

        elif user_number < random_number:
            count += 1
            if count == 4 or count == 5:
                print('\n'f'У Вас осталось', 7 - count, 'попытки.''\n')
            elif count == 6:
                print('\n'f'У Вас осталось', 7 - count, 'попытка.''\n')
            elif count == 7:
                print('Вы исчерпали 6 попыток. Игра окончена.')
                print('Число которое было загадано:', random_number)
                break
            print('Вы ввели число меньше! Попробуйте ещё раз.')
            user_number = input('Введите число: ')
            user_number = number_control(user_number)
            user_number = int(user_number)

        elif user_number == random_number:
            print('Вы угадали! Ураа!')
            os.system('cls')
            break

    print('Хотите сыграть ещё раз?')
    replay_the_game = input('Введите ЦИФРУ для ПРОДОЛЖЕНИЯ ИГРЫ, любой СИМВОЛ для ВЫХОДА. ')
    if replay_the_game.isdigit():
        print('Удачной игры.')
        time.sleep(3)
        os.system('cls')
    elif not replay_the_game.isdigit():
        print('Спасибо за игру. До свидания!')
        os.system('cls')
        break

