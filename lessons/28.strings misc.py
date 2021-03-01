a = "Pular\nde linha\t e tab\n\\\n\'"
print(a)
print(r"Pular\nde linha\t e tab\n\\\n\'")
print('''Pular de linhas
	de jeito fácil.''')

a.upper()

a.isupper()

a.lower().islower()

a.isalpha() #só letras
a.isalnum() #somente letras e numeros
a.isdecimal() #só numeros
a.isspace() #espaço em branco
a.istitle() #primeira maiúscula de todas palavras

a.startswith('Pular')
a.endswith('\'')


'-'.join(['a', 'b', 'c'])

'Sobre este curso'.split()
'Sobre este curso'.split('e')

'Oi'.ljust(20)
'Oi'.rjust(20)
'Oi'.center(20, '=')


'                  Oi'.lstrip()
'                  Oi                  '.rstrip()
'aaaaVictoraaaaaa'.strip('a')

'banana'.replace('a', 'o')


nome='Victor'
hora='7pm'
comida='salaminho'

print('Oi, '+nome+'. A festa será às '+hora+' e teremos '+comida+'.')
print('Oi, %s. A festa será às %s e teremos %s.' % (nome, hora, comida))