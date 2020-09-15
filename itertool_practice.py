# import numpy as np
# Set jako element usprawniający pracę na listach danych

# list_a = ['Bulbasaur', 'Charmander', 'Squirtle']
# list_b = ['Caterpie', 'Pidgey', 'Squirtle']
# set_a = set(list_a)
# set_b = set(list_b)
# print(set_a.intersection(set_b))
# print(set_a.difference(set_b))
# print(set_a.union(set_b)) #pomijanie wielokrotnych wystąpień

# Elimacja pętli
"""Eliminacja pętli sprawi, że kod będzie bardziej czytelny i przejrzysty 'Flat is better than nested'"""

poke_stats = [
    [90, 92, 75, 60],
    [25, 20, 15, 90],
    [65, 130, 60, 75]]

# Sumowanie po wierszu za pomocą pętli
totals = []
for row in poke_stats:
    totals.append(sum(row))

print(totals)
# List comprehension - sumowanie po wierszu
total_comp = [sum(row) for row in poke_stats]
print(total_comp)

# Sumowanie po wierszu za pomocą funkcji map

# total_map = [map(sum, poke_stats)]
# print(total_map)
#
# print(poke_stats.mean(axis=1))

# names = ['Absol', 'Aron', 'Jynx', 'Natu', 'Onix']
# attacks = np.array([130, 70, 50, 50, 45])

# print(zip(names,attacks))

# Armstrong numbers
"""
Wyszukiwwanie licz będących liczbami Armstronga

Link
-----
https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap04/arms.html
"""

# def arm_nums(inputed_num):
#     arm_list = []
#     for digit in str(inputed_num):
#         arm_list.append(int(digit))
#     list_len = len(arm_list)
#     comp_list = map(lambda x: x**list_len, arm_list) #użycie funkcji lambda na liscie danych
#     comp_list_sum = sum(comp_list)
#     if comp_list_sum == inputed_num:
#         print('{} is Armstrong Number'.format(comp_list_sum))

# Testowanie kodu
# for i in range(1,10000):
#     arm_nums(i)

#
# def factorization(num):
#     for i in range(1, num+1):
#         if num % i == 0:
#             print('{} is a factor'.format(i))
# factorization(12)


# Prime number generator

# def prime_number(prim_num):
#     factors = 0
#     prime_list = []
#
#     for i in range(1, prim_num+1):
#         if prim_num % i == 0:
#             prime_list.append(i)
#             factors += 1
#     print(factors)
#     if factors == 2:
#         print('{} is prime'.format(str(prim_num)))
#     else:
#         print('{} is not prime'.format(str(prim_num)))
#     print(prime_list)

# import time
# #Prime number generator with nested loop
#
# insert_num = input('Proszę wprowadzić wartość int')
# start = time.time()
# prime_list = []
# for num in range(1, 101):
#     factors = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors += 1
#     if factors == 2:
#         prime_list.append(num)
# end = time.time()
# print(prime_list)
# print(len(prime_list))
# print('Czas wykonania programu to {} (sekundy): '.format(end-start))

# -----------------------------------------------------#
# Pyramid function
#
# for i in range(0,11):
#     pyramid = '*' + i * '**'
#     print(pyramid.center(21,' '))
#

# def pyramid_hight():
#     hight = int(input('Wprowadź wysokość piramidy: '))
#
#     for i in range(0, hight):
#         pyramid = '*' + i * '**'
#         print(pyramid.center(2*hight, ' '))
# #Tesowanie
# pyramid_hight()

# -----------------------------------------------------#
# Window function
"""Zaproponowana funkcja wydaje się zbyt skomplikowana"""


# def columns(col_num):
#     for num in range (1,col_num):
#         print('x',end='')
#         for i in range(1,10):
#             print('-', end='')
#     print('x',end='')
#
# def row_num(row_num):
#     for num in range (1,row_num):
#         print('x',end='\n')
#         for i in range(1,5):
#             print('|', end='\n')
#     print('x',end='\n')

# -----------------------------------------------------#
# Window function - updated

def row(d):
    print('+' + d * '----------+')


def col(d):
    print('|' + d * '          |')


def windowWide(d):
    row(d)
    for i in range(1, 6):
        col(d)
    # return col(d)


def window(w, h):
    for i in range(0, h):
        windowWide(w)
    row(w)


# Tesowanie funkcji
# window(3, 5)


# -----------------------------------------------------#
# String-counter

def string_counter():
    text = input("Wprowadź tekst dla którego chcesz wyszukiwać poszczególnego znaku: ")
    letter = input("Wprowadź szukany znak: ")
    count = 0
    for i in text.lower():
        if i == letter:
            count += 1
    print(count)


# String-counter Test
# string_counter()


def fix_capitalize(paragraph):
    paragraph_list = list(paragraph)
    paragraph_list.append(' ')
    paragraph_list.append(' ')

    paragraph_list[0] = paragraph_list[0].capitalize()
    for i in range(0, len(paragraph_list)):  # wyszukanie kropek
        if paragraph_list[i] == '.':
            print(i)
            c = paragraph_list[i + 2]
            c = c.capitalize()
            paragraph_list[i + 2] = c
    paragraph_list = ''.join(paragraph_list)
    return (paragraph_list)


p = "djokovic has been lock in an incredible rivalry ' \
            'with Federer and Rafael Nadal for over a decade with them sharing an' \
            ' astonishing 56 Grand Slam titles between them. it is Federer, though,' \
            ' who currently leads the way with 20, three head of Djokovic, but Roccardo Piatti,' \
            ' who worked with Djokovic earlier in his career, thinks all that is about to change."

# Test
fix_capitalize(p)

# String counter

import re


def count_word(pattern, text):
    pattern = pattern + '+'
    print(pattern)
    text = text.lower()
    count = 0
    for match in re.finditer(pattern, text):
        count += 1
    print('{} liczba powtórzen słowa {}'.format(count, pattern[:-1]))


# Test
# text = 'Stuff? Yes, man i like stuff. Stuffifaf, stuff!'
# count_word('stuff', text)

# -----------------------------------------------------#
# Word Top 10 ranking - Harry Potter

import string

text = open('Harry_Potter.txt', 'r')
text = text.read()
words = []
dictionary = {}

def removePunctuation(st):
    for c in string.punctuation:
        st = st.replace(c, '')
    return st

def lowerSplit(st):
    st = st.lower()
    st = st.split()
    return st

def countWord(word, st):
    count = st.count(word)
    return count

text = removePunctuation(text)
text = lowerSplit(text)


print(text)

from collections import Counter

cnt = Counter()
for i in text:
    cnt[i] += 1
print(cnt.most_common(10))
