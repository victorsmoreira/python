# Esse programa diz Olá e pergunta seu nome

print("Olá!")
print("Qual é o seu nome?") # Pergunta pelo nome
seuNome = input()
print("Prazer em conhecê-lo, " + seuNome)
print("Seu nome tem " + str(int(len(seuNome))) + " letras.")
print("Qual é a sua idade?") # pergunta pela idade
suaIdade = input()
print("Você terá " + str(int(suaIdade) + 10) + " anos em 2030")
fim = input()