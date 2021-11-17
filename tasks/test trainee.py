# import random

# def polindrom_srt(str):
#     str = str.replace(" ", "")
#     length = len(str)
#     for i in range(0, length//2):
#         a = str[i]
#         b = str[length-i-1]
#         print(a, b)
#         if a != b:
#             return False
#     return True
#
#
# str = "never odd or even"
# print(polindrom_srt(str))


def symmetry_srt(a):
    a = a.replace(" ", "")
    length = len(a)

    if length % 2:
        mid = length//2 + 1
    else:
        mid = length//2
    start1 = 0
    start2 = mid
    while start1 < mid and start2 < length:
        if a[start1] == a[start2]:
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            return False
    return True

print(symmetry_srt("amaama"))


# def symmetry(a):
#     n = len(a)
#     flag = 0
#
#     # Check if the string's length
#     # is odd or even
#     if n % 2:
#         mid = n // 2 + 1
#     else:
#         mid = n // 2
#
#     start1 = 0
#     start2 = mid
#
#     while (start1 < mid and start2 < n):
#
#         if (a[start1] == a[start2]):
#             start1 = start1 + 1
#             start2 = start2 + 1
#         else:
#             flag = 1
#             break
#
#     # Checking the flag variable to
#     # check if the string is symmetrical
#     # or not
#     if flag == 0:
#         print("The entered string is symmetrical")
#     else:
#         print("The entered string is not symmetrical")
#
#
# # Driver code
# string = 'amaama'
# symmetry(string)



def narcissistic_number(number: int):
    string = str(number)
    length = len(string)
    number_sum = 0
    for i in range(0, length):
        number_sum += int(string[i]) ** length

    return number_sum == number


print(narcissistic_number(407))




# list1 = [1, 2, 3]
# list2 = [1, 2, 5, 6, 7]
#
#
# def lists(list1, list2):
#     result = []
#     for el1 in list1:
#         for el2 in list2:
#             if el1 == el2:
#                 result.append(el1)
#     return result
#
#
# print(lists(list1, list2))
#
#
# # string = list(random.choice(string.ascii_letters())
#
# def random_string (list):
#     result = ""
#     for i in range(4):
#         result = result + random.choice(list)
#     return result
#
# print(random_string(['0','1','2','B','C','D','P','Q','R']))
#
#
# def great_number(list):
#     return "".join(sorted(list, key=lambda x: x[0], reverse=True))
#
#
# print(great_number(list = ["5", "12", "74", "888"]))
#
#
# def symmetric_list(list):
#     for i in range(round(len(list)/2)):
#         if list[i] != list[len(list)-i-1]:
#             return False
# sorted()
#     return True
#
# print(symmetric_list(list=["a", "b", "c", "b", "a"]))
#
#
#
#
#
#
# string = "String"
# print(string)
# print(string[0::-1])
#
#
#
#
#
#
# hotels = [{'name': 'Hilton', 'locations': 2345}, {'name': 'Accor', 'locations':789}, {'name': 'W', 'locations':678}]
# hotel_names = []
# for hotel in hotels:
#     hotel_names.append(hotel["name"])
# print(hotel_names)
#
#
# hotel_names = [hotel["name"] for hotel in hotels]
# print(hotel_names)
#
#
# hotel_names = list(map(lambda h: h["name"], hotels))
# print(hotel_names)
#
#
#
#
# def word_count(string):
#     result = dict()
#     words = string.split(" ")
#     for word in words:
#         if word not in result:
#             result.setdefault(word, 1)
#         else:
#             result[word] = result[word] + 1
#     return result
#
# result = word_count(" Write a function named word_count() that takes in a string. Return a dictionary with each word in the string as the key and the number of times it appears as the value.")
# print(result)
#
#
#
# def flip_flop(dictionary):
#     result = {}
#     for el in dictionary:
#         result.setdefault(dictionary[el], el)
#     return result
#
# def meta_flip_flop(dictionary):
#     result  = dict()
#     for el in dictionary:
#         if type(dictionary[el]) == dict:
#             result.setdefault(el, flip_flop(dictionary[el]))
#         else:
#             result.setdefault(dictionary[el], el)
#     return result
#
# res = meta_flip_flop({"apple": 1, "book": 2, 'box': {'WWW':1} })
# print(res)
#
# """
#
# 4. Given the list below, write code to remove duplicates and preserve initial order of elements occurrence.
#
# amenities = ['free wifi', 'breakfast', 'gym', 'breakfast', 'pool', 'restaurant']
#
#
#
#
# 5. Write a decorator that will print the execution duration of the method it decorates.
#
#
#
# 6. Write a function that will remember parameters passed to it and if such parameters have already been passed - will not waste time on their calculation in a second time. Do not use ready-made solutions, but make yours.
# As an example, you can take the following function:
#
#
# from time import sleep
#
# def delayed_greeting(name):
#     sleep(5)
#     return f'Hey, {name}!'
# delayed_greeting('Bob')
# delayed_greeting('Bob')
#
# # It takes ~ 10 seconds before optimization.
# # It should take ~ 5 seconds after optimization.
# # sleep(5) removing is not considered optimization :)
# # you can use decorator from previous task for self-testing
#
# 7. Write a function that takes a list of numbers, and for each list element it should find the product of rest list elements excluding the current one.
#
# For example, given: [2, 5, 3, 4]
# Your function should return: [60, 24, 40, 30]
# By calculating: [5 * 3 * 4,  2 * 3 * 4,  2 * 5 * 4,  2 * 5 * 3]
#
#
# ***