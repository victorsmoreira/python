import pprint

mensagem = 'Câmara dos EUA aprova segundo impeachment de Trump; processo segue para o Senado'
count = {}

for letra in mensagem.upper():
	count.setdefault(letra, 0)
	count[letra] += 1

pprint.pprint(count)

org = pprint.pformat(count)
print(org)