lista = ['gato', 'rato', 'ave', 'cobra']

print('lista = ' + str(lista))

print('lista[0] = ' + lista[0])
print('lista[2] = ' + lista[2])

print('lista[-1] = ' + lista[-1])
print('lista[-2] = ' + lista[-2])

print('lista[1:3] = ' + str(lista[1:3]))

i = 2
lista[i] = 'baleia'
print('i=2; lista[i] = baleia; lista = ' + str(lista))

lista[2:5] = ['a', 'b', 'c']
print('lista[2:5] = [a,b,c]; lista = ' + str(lista))

print('lista[:2] = ' + str(lista[:2]))

del lista[1]
print('del lista[1] = ' + str(lista))

print('len(lista) = ' + str(len(lista)))

lista = lista + [1,2,3]
print('lista + [1,2,3] = ' + str(lista))

lista = lista * 2
print('2*lista = ' + str(lista))

print('list("soletra") = ' + str(list("soletra")))