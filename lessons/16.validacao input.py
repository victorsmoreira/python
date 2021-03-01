print('Quantos gatos vc tem?')
numGatos = input()
try:
	if int(numGatos) >= 3:
		print('São muitos gatos')
	else:
		print('Poucos......')
except ValueError:
	print(numGatos, 'não foi reconhecido como um número')