import re

infCpl = 'PV3372. Local de entrega.: Rua Trairas, 42 - Carlos Prates, Belo Horizonte - MG, 30810-190'
#infCpl = 'Local de entrega.: Rua Trairas, 42 - Carlos Prates, Belo Horizonte - MG, 30810-190'


PV=re.compile(r'(\d\d)(\d\d)') #se precisar buscar (), utilizar \(\)
#PV=re.compile(r'\d{4}')
mo=PV.search(infCpl[0:10]) #PV.search procura a 1a ocorrencia. Usar PV.findall para procurar todas ocorrências

if mo == None:
	print('Sem PV')
else:
	print(mo.group())
	print('primeiros 2 dígitos são %s' % mo.group(1))
	print('2 últimos dígitos são %s' % mo.group(2))



fone='Meu telefone é 98648-8467'
#fone='Meu telefone é (31) 98648-8467'
foneRegExpr = re.compile(r'(\(\d\d\) )?\d\d\d\d\d-\d\d\d\d') #?:0 ou uma vez
mo = foneRegExpr.search(fone)
print(mo.group())



batRegExpr = re.compile(r'Bat(wo)*man') #*:0 ou mais vezes; +:1 ou mais vezes
mo1 = batRegExpr.search('Aventuras do Batman')
print(mo1.group())
mo2 = batRegExpr.search('Aventuras da Batwowowowoman')
print(mo2.group())



haRegExpr = re.compile(r'(ha){1,3}?') #?procura o menor valor (1, no caso). Sem o ?, procura o maior valor
moha = haRegExpr.search('haha')
#moha = haRegExpr.search('hahahahahaha')
print(moha.group())



fone='Meus telefones são (31) 98648-8467 e (31) 3234-6285'
foneRegExpr = re.compile(r'((\(\d\d\) )?(\d)?(\d\d\d\d-\d\d\d\d))')
mo = foneRegExpr.findall(fone)

todostelefones = []
for telefone in mo:
	todostelefones.append(telefone[0])

print(todostelefones)