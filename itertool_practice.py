#import numpy as np
#Set jako element usprawniający pracę na listach danych

# list_a = ['Bulbasaur', 'Charmander', 'Squirtle']
# list_b = ['Caterpie', 'Pidgey', 'Squirtle']
# set_a = set(list_a)
# set_b = set(list_b)
# print(set_a.intersection(set_b))
# print(set_a.difference(set_b))
# print(set_a.union(set_b)) #pomijanie wielokrotnych wystąpień

#Elimacja pętli
"""Eliminacja pętli sprawi, że kod będzie bardziej czytelny i przejrzysty 'Flat is better than nested'"""

poke_stats = [
    [90, 92, 75, 60],
    [25, 20, 15, 90],
    [65, 130, 60, 75]]

#Sumowanie po wierszu za pomocą pętli
totals = []
for row in poke_stats:
    totals.append(sum(row))

print(totals)
#List comprehension - sumowanie po wierszu
total_comp = [sum(row) for row in poke_stats]
print(total_comp)

#Sumowanie po wierszu za pomocą funkcji map

# total_map = [map(sum, poke_stats)]
# print(total_map)
#
# print(poke_stats.mean(axis=1))

# names = ['Absol', 'Aron', 'Jynx', 'Natu', 'Onix']
# attacks = np.array([130, 70, 50, 50, 45])

# print(zip(names,attacks))

#Armstrong numbers
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

#Testowanie kodu
# for i in range(1,10000):
#     arm_nums(i)

#
# def factorization(num):
#     for i in range(1, num+1):
#         if num % i == 0:
#             print('{} is a factor'.format(i))
# factorization(12)



#Prime number generator

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

#-----------------------------------------------------#
#Pyramid function
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

#-----------------------------------------------------#
#Window function
def columns(col_num):
    for num in range (1,col_num):
        print('x',end='')
        for i in range(1,10):
            print('-', end='')
    print('x',end='')

def row_num(row_num):
    for num in range (1,row_num):
        print('x',end='\n')
        for i in range(1,5):
            print('|', end='\n')
    print('x',end='\n')

columns(3)
row_num(4)
row_num(4)
row_num(4)
columns(3)
