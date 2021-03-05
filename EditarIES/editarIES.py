import os
import pprintpp as pp
import pandas as pd

#	LISTAR ARQUIVOS
pastaIES = 'IES_atual'
novosIES = 'IES_corrigido'

todos_arquivos = {}

for pasta, subpasta, arquivo in os.walk(pastaIES):
	try:
		os.makedirs(novosIES+'\\'+pasta[len(pastaIES)+1:])
	except FileExistsError:
		pass

	for i in arquivo:
		if i[-4:].lower() == '.ldt':
			continue
		else:
			info_arquivo = {}
			info_arquivo['Caminho']=str(os.path.join(pasta, i))
			todos_arquivos[i] = info_arquivo

#	INSERIR CÓDIGO NO DFs
arquivo_correl = 'IES_info_a_corrigir.xlsx'
xls = pd.ExcelFile(arquivo_correl)
df = xls.parse(xls.sheet_names[0])
df = df[~df['IES'].isin(['-'])]
correl = df.set_index('IES').to_dict()['Código']

cod_enc = 0
cod_nenc = 0
for nome_IES in todos_arquivos:
	try:
		IES_correl = nome_IES[:-4]
		todos_arquivos[nome_IES]['Código'] = correl[IES_correl]
		cod_enc = cod_enc + 1
	except:
		cod_nenc = cod_nenc + 1
print(f'{cod_enc} com código e {cod_nenc} arquivos sem código')


#	LER CONTEÚDO DO ARQUIVO
for nome_IES in todos_arquivos:
	caminho = todos_arquivos[nome_IES]['Caminho']
	abrir_arquivo = open(caminho, 'r')
	conteudo = abrir_arquivo.readlines()

	nlin = 10		#nº de linhas para ler no arquivo
	
#	PADRONIZAR NOME DO FABRICANTE
	for l in range(nlin):
		if '[MANUFAC]' in conteudo[l]:
			conteudo[l] = '[MANUFAC] LeoMoon Studios\n'
			break

#	INSERIR CÓDIGO NA CHAVE [LUMCAT]
	if any('[LUMCAT]' in s for s in conteudo[:nlin]):
		for i in range(nlin):
			if '[LUMCAT]' in conteudo[i]:
				try:
					conteudo[i] = '[LUMCAT] ' + todos_arquivos[nome_IES]['Código'] + '\n'
					break
				except:
					conteudo[i] = '[LUMCAT] Sem código\n'
					break
	else:
		for j in range(nlin):
			if '[MANUFAC]' in conteudo[j]:
				try:
					conteudo.insert(j+1, '[LUMCAT] ' + todos_arquivos[nome_IES]['Código'] + '\n')
					break
				except:
					conteudo.insert(j+1, '[LUMCAT] Sem código\n')
					break

#	ESCREVER NOVO ARQUIVO
	with open(novosIES+'\\'+caminho[len(pastaIES)+1:], 'w') as f:
		for i in conteudo:
			f.write(f'{i}')