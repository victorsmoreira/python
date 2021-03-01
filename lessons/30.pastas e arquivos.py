import os
import shutil

os.path.join('pasta1', 'pasta2', 'pasta3', 'arquivo.ext')
os.sep()
os.getcwd()
op.chdir('C:\\')
# C:\Users\victo\OneDrive\Área de Trabalho\Pessoal\Python

# .\ pasta atual
# ..\ pasta acima

os.path.abspath()
os.path.isabs()
os.path.dirname()
os.path.basename()
os.path.exists()
os.path.isfile()
os.path.isdir()
os.path.getsize()
os.walk()

os.lisdir() #lista pastas e arquivos

os.makedirs() #cria pastas

arquivo = open('c:\\Users\\victo\\oi.txt', 'a')	# abrir, 'w' para sobrescrever, 'a' para append
arquivo.read()								# ler
arquivo.write('lalala')						# escrever
arquivo.close()								# fechar


# import shelve para arquivos com dados complexos (dicionários, listas)


# deletes

shutil.copy('origem', 'destino\\(renomear)?')
shutil.copytree('or', 'dest')
shutil.move('or', 'dest\\(renomear)?') #para renomear, usar a mesma origem e destino


os.unlink('arquivo')
os.rmdir('arquivo')
shutil.rmtree('pasta')


	# usar dry run ao usar essas funções: comentar o comando e fazer um print no lugar.	