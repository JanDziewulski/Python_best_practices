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

total_map = [map(sum, poke_stats)]
print(total_map)
