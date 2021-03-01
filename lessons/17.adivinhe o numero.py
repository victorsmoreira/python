#Jogo de adivinhar o numero
import random
print('Olá! Qual é o seu nome?')
nome = input()
print('Oi, '+ nome + ('! Estou pensando em um número entre 1 e 20, tente adivinhar!'))

solucao = random.randint(1,20)

for i in range (1,6):
	if i < 6:
		tentativa = input()
		try:
			if int(tentativa) > solucao:
				print('Palpite muito alto.')
			elif int(tentativa) < solucao:
				print('Palpite muito baixo.')
			else:
				break
				
		except ValueError:
			print(tentativa + ' não é um número.')
	
if tentativa == solucao and i == 1:
	print('Parabéns, você acertou em '+ str(i) + ' tentativa')	
elif int(tentativa) == solucao:
	print('Parabéns, ' + nome + '! Você acertou em '+ str(i) + ' tentativas')
else:
	print('Infelizmente você não acertou, ' + nome + '. O número que eu estava pensando era o' + solucao)