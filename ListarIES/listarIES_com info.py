import os
import pandas as pd


pastaNacIES = 'IESNac'
pastaMGIES = 'IESMG'
nlin = 10		#nº de linhas para ler nos arquivos
IESNac = {}
IESMG = {}


# função ler arquivos
def listar_arquivos(pasta_a_ler, dicionario):
	for pasta, subpasta, arquivo in os.walk(pasta_a_ler):
		for i in arquivo:
			info_arquivo = {}
			info_arquivo['Caminho']=str(os.path.join(pasta, i))
			dicionario[i] = info_arquivo


# função para pegar [LUMCAT] e [MANUFAC]
def pegar_infos(dicionario):
	for nome_IES in dicionario:
		caminho = dicionario[nome_IES]['Caminho']
		abrir_arquivo = open(caminho, 'r')
		conteudo = abrir_arquivo.readlines()
		# MANUFAC
		for k in range(nlin):
			if '[MANUFAC]' in conteudo[k]:
				dicionario[nome_IES]['MANUFAC'] = conteudo[k][:-1]
				break
		# LUMCAT
		if any('[LUMCAT]' in r for r in conteudo[:nlin]):
			for k in range (nlin):
				if 'LUMCAT' in conteudo[k]:
					try:
						dicionario[nome_IES]['LUMCAT'] = conteudo[k][:-1]
						break
					except:
						dicionario[nome_IES]['LUMCAT'] = 'Sem LUMCAT'
						break


# Nacional
listar_arquivos(pastaNacIES, IESNac)
pegar_infos(IESNac)

# MG
listar_arquivos(pastaMGIES, IESMG)
pegar_infos(IESMG)


# Transformar em df para exportação:
df_Nac = pd.DataFrame(IESNac).T
df_MG = pd.DataFrame(IESMG).T


# Exportar para excel
writer = pd.ExcelWriter('Aquivos listados com info.xlsx', engine = 'xlsxwriter')

df_MG.to_excel(writer, sheet_name='MG', index = True)
df_Nac.to_excel(writer, sheet_name='Nac', index = True)

writer.save()