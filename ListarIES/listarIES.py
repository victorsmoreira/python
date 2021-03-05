import os
import pprintpp as pp
import pandas as pd

# # lambda:
# for sublist in i:
#     for item in sublist:
#         IESnac.append(item)

pastanacIES = 'IESNac'
pastaMGIES = 'IESMG'

# Listar arquivos nacional
IESnac = []
i = []
for pasta, subpasta, arquivo in os.walk(pastanacIES):
	i.append(arquivo)

IESnac = lambda i: [item for sublist in i for item in sublist]

# Listar arquivos MG
IESMG = []
j = []
for pastaMG, subpastaMG, arquivoMG in os.walk(pastaMGIES):
	j.append(arquivoMG)

IESMG = lambda j: [itemMG for sublistMG in j for itemMG in sublistMG]

# Jogar valores da função lambda na variável e montar o df
IESnac = IESnac(i)
df_nac = pd.DataFrame(IESnac)
df_nac.columns = ['Arquivos Nac']
df_nac.sort_values(by=['Arquivos Nac'], inplace=True, ignore_index=True)


IESMG = IESMG(j)
df_MG = pd.DataFrame(IESMG)
df_MG.columns = ['Arquivos MG']
df_MG.sort_values(by=['Arquivos MG'], inplace=True, ignore_index=True)

# print(df_MG.loc[50]['Arquivos MG'])

# df = df_MG
# for i in range(len(df_nac)):
# 	df.at[i,'Arquivos Nac'] = df_nac.loc[i]['Arquivos Nac']

df = pd.concat([df_MG, df_nac], axis=1)

# Exportar para excel
writer = pd.ExcelWriter('Arquivos listados.xlsx', engine = 'xlsxwriter')

df.to_excel(writer, sheet_name='Concat', index = True)
df_MG.to_excel(writer, sheet_name='MG', index = True)
df_nac.to_excel(writer, sheet_name='Nac', index = True)


writer.save()