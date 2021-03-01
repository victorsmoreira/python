Gata = {'nome':'Lasanha', 'caracteristica':'faminta','idade':2}
print(Gata['nome'])

Gatinha = {'caracteristica':'faminta', 'idade':2, 'nome':'Lasanha'}
print(Gata == Gatinha)

print(list(Gata.keys()))

print(list(Gata.values()))

print(list(Gata.items()))

for i, k in Gata.items():
	print(i, k, sep='=')

print(Gata.get('nome', 'ñ enc'))
print(Gata.get('peso', 'ñ enc'))

Gata.setdefault('nome', 'sem nome')
print(Gata)
Gata.setdefault('cor', 'cinza e branco')
print(Gata)