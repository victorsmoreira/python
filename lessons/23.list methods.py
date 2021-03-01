spam = ['a', 'b', 'c', 'd', 'a']

print(spam.index('c'))
print(spam.index('a')) #encontra apenas o primeiro index


spam.append('f')
print(spam)

spam.insert(5, 'e')
print(spam)

spam.remove('a')
print(spam)
del spam[5]
print(spam)

spam.sort() # = sorted(spam)
print(spam)

spam.sort(reverse=True) # = sorted(spam, reverse=True)
print(spam)

lista = ['Victor', 'Arthur', 'Horácio', 'verde', 'humano', 'arco']
print(sorted(lista))
lista.sort(key=str.lower)
print(lista)