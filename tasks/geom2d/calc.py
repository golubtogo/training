import collections
from backport_collections import Counter


# def calc1():
#     x = ((67+33)*(25-20))/25
#     print(x)


# def count_num(a, b):
#     a = 117
#     b = 23
#     print(a % b)


# Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
# x = ((67+33)*(25-20))/25
# ((67+33)*(25-20))/25
# 20.0
# (4+5*60-17+65/4) ** 0.5
# 17.414074767267998


# n = 6.996+45*(13/2) ** 2 + 2* 18 ** 0.5
# round(n, 3)
# 1916.731


# a = (1267-20*((5**3)/2)**2) / ((8**5) * (36**0.5))
# round(a, 3)
# -0.391

# b = ((((9**0.5)**3)**2)**2) / (-2)**-3
# round(b, 3)
# -4251528.0


# string_1 = 'Hello, world!'
# string_2 = 'Python <3'
# string_3 = 'qwerty'
#
# print((len(string_1)*len(string_2)*len(string_3))**(1/3))
# 8.88748820522211

def power_str(string: str, power: int):
    length = len(string)
    len_power = length**power
    print(string, length, len_power)


power_str('Привет!', 5)


def is_word_long(string: str, number: int):
    length = len(string)
    if length <= number:
        print("Это слово короткое.")
    else:
        print("Это слово длинное.")


is_word_long('ОченьДлинноеСлово', 7)


def rare_word(word: str):
    if "ф" in word:
        print("Ого! Вы ввели редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")


rare_word('ОченьДлинноеСлово')
rare_word('фонтан')


def latter_in_word(word: str, letter: str):
    if letter in word:
        print("Выбранная буква есть в введённом слове")
    else:
        print("Выбранной буквы нет в введённом слове")


latter_in_word('ОченьДлинноеСлово', 'и')
latter_in_word('фонтан', 'и')


def num_is_integer(number: int):
    result = number**0.5
    if result == int(result):
        print(int(result))
    else:
        print("Квадратный корень из ", number, " не целое число")


num_is_integer(169)


day_week = 5
if day_week == 1:
    print("понедельник")
elif day_week == 2:
    print("вторник")
elif day_week == 3:
    print("среда")
elif day_week == 4:
    print("четверг")
elif day_week == 5:
    print("пятница")
elif day_week == 6:
    print("субота")
elif day_week == 7:
    print("воскресенье")


def is_weight_good(weight: float, height: float):
    index_count = weight/height**2

    if 18.5 <= index_count <= 24.99:
        print("Норма")
    elif index_count < 18.5:
        print("Недостаточная масса тела")
    elif index_count > 24.99:
        print("Избыточная масса тела")


is_weight_good(80, 1.8)


def is_mark(mark: int):

    if 4 <= mark <= 5:
        print("удовлетворительно")
    elif 6 <= mark <= 7:
        print("хорошо")
    elif mark < 4:
        print("неудовлетворительно")
    elif mark >= 8:
        print("отлично")


is_mark(7)


def is_balance(balance: int):

    if balance >= 5000:
        print("Сегодня твой выбор - ресторан!")
    elif 2500 <= balance <= 5000:
        print("Эх, только фастфуд.")
    elif balance < 2500:
        print("Придется потерпеть!")


is_balance(455)


def divide_num(number: int):

    if number % 2 == 0:
        print("Число делится на 2 без остатка.")
    elif number % 3 == 0:
        print("Число делится на 3 без остатка.")
    elif number % 5 == 0:
        print("Число делится на 5 без остатка.")
    else:
        print("Число не делится ни на 2, ни на 3, ни на 5 без остатка!")


divide_num(int(452))


def favor_flower(flower: str, color: str):
    if flower == 'роза' and (color == 'белые' or color == 'синие'):
        print("Ане понравятся эти цветы")
    else:
        print("Аня не любит такие цветы")


favor_flower("роза", "фиолетовый")
favor_flower("роза", "синие")
favor_flower("пион", "синие")


def find_man(height: int, weight: int, color: str):
    if height > 170 and (weight < 80 and color == 'синий'):
        print("Ваша половинка нашлась!")
    else:
        print("Попробуем поискать ещё...")


find_man(180, 70, "синий")


def find_number(number: int):
    if number % 2 == 0 or number % 5 == 0 or number % 173 == 0 or number % 821 == 0:
        print("Вова, это нужное число")
    else:
        print("Вова, в этот раз ты не попал")


find_number(346)


def fav_word(word: str):
    if word == "рептилия" or word == "питон" or word == "змея":
        print("Python")
    elif word == "плюс" or word == "плюсы":
        print("C++")
    elif word == "рубин" or word == "кристалл":
        print("Ruby")
    else:
        print("Python")


fav_word('Аппликация')
fav_word('рубин')


def free_time(hour, minute):
    time = str(hour) + ":" + str(minute)
#    if 10 <= hour >= 20:
    if (time >= "10:30" and time <= "12:00") or (time >= "13:40" and time <= "15:00") or (time >= "18:00" and time <= "19:30"):
        print("Преподаватель занят.")
    else:
        print("Преподаватель свободен.")


free_time(19, 55)


def secret_word(word: str):
    for i in range(0, len(word), 2):
        print(word[i])


secret_word('подшипник')



# Implement the transformer allows us to get "4a2b5c1d" by "aaabbcccccda" in the following way:
# <number of characters in the string><character>.......\



def count_letters(word: str):
        l = Counter(word)
        print(l.items())

count_letters("aaabbcccccda")
























