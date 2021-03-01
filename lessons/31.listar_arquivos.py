import os
import pprintpp as pp

todos_arquivos = []
for pasta, subpasta, arquivo in os.walk('C:\\Users\\victo\\OneDrive\\Área de Trabalho\\IES MG (jun 2020)'):
	for i in arquivo:
		todos_arquivos.append(i)
		# print(i)
pp.pprint(todos_arquivos)